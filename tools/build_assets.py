#!/usr/bin/env python3
"""캐릭터 스프라이트 누끼·정렬·WebP 내보내기, 배경 리사이즈."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAW = "../downloads/hospital-vn-raw"
OUT = "assets/img"

CHARS = {
    "haram": ["base", "blush", "surprised", "serious"],
    "serin": ["base", "blush", "surprised", "serious"],
}
BGS = ["bg_ward_day", "bg_ward_night", "bg_rooftop_dusk", "bg_er_night"]

MX_T, SAT_T, ERODE, BLUR = 246, 9, 5, 0.8


def alpha_of(path):
    """흰 배경을 안쪽부터 채워 실루엣을 잡고, 테두리 색을 안쪽 색으로 바꾼다."""
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    mx = a.max(axis=2)
    mn = a.min(axis=2)
    ink = (mx < MX_T) | ((mx - mn) > SAT_T)

    m = Image.fromarray(np.where(ink, 255, 0).astype(np.uint8), "L")
    w, h = m.size
    padded = Image.new("L", (w + 2, h + 2), 0)
    padded.paste(m, (1, 1))
    ImageDraw.floodfill(padded, (0, 0), 128, thresh=0)
    bg = (np.asarray(padded) == 128)[1:-1, 1:-1]

    al = Image.fromarray(np.where(~bg, 255, 0).astype(np.uint8), "L")
    al = al.filter(ImageFilter.MinFilter(ERODE)).filter(ImageFilter.GaussianBlur(BLUR))

    alpha = np.asarray(al).astype(np.float32)
    rgb = np.asarray(im).astype(np.float32)

    # 테두리 색 오염 제거: 불투명 픽셀 색을 바깥으로 8px 번지게 채운다
    core = alpha > 235
    filled = rgb.copy()
    have = core.copy()
    for _ in range(8):
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            s_rgb = np.roll(filled, (dy, dx), axis=(0, 1))
            s_have = np.roll(have, (dy, dx), axis=(0, 1))
            take = (~have) & s_have
            filled[take] = s_rgb[take]
            have = have | take
    edge = (~core) & (alpha > 0)
    out = rgb.copy()
    out[edge] = filled[edge]

    arr = np.dstack([out.astype(np.uint8), alpha.astype(np.uint8)])
    return Image.fromarray(arr, "RGBA")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, exprs in CHARS.items():
        base = alpha_of(os.path.join(RAW, f"ch_{name}_base.png"))
        bbox = base.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
        pad = 10
        box = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
               min(base.width, bbox[2] + pad), min(base.height, bbox[3] + pad))
        size = (box[2] - box[0], box[3] - box[1])
        target_h = 1400
        tw = round(size[0] * target_h / size[1])
        for e in exprs:
            rgba = alpha_of(os.path.join(RAW, f"ch_{name}_{e}.png"))
            rgba = rgba.crop(box).resize((tw, target_h), Image.LANCZOS)
            out = os.path.join(OUT, f"{name}_{e}.webp")
            rgba.save(out, "WEBP", quality=90, method=6)
            print(f"{name}_{e}", rgba.size, os.path.getsize(out))

    for b in BGS:
        im = Image.open(os.path.join(RAW, f"{b}.png")).convert("RGB")
        im = im.resize((1536, 864), Image.LANCZOS)
        out = os.path.join(OUT, f"{b.replace('bg_', '')}.webp")
        im.save(out, "WEBP", quality=85, method=6)
        print(b, os.path.getsize(out))


if __name__ == "__main__":
    main()
