#!/usr/bin/env python3
"""Scenario authoring DSL + JSON builder.

Each scene module exposes build(S). S.line() appends a node; by default a node
flows into the next appended node. S.choice() attaches choices to the previous
line. Labels make jump targets readable; they are resolved at the end.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import s0_prologue, s1_day1, s2_night1, s3_day2, s4_dawn, s5_lastday  # noqa: E402


class Scene:
    def __init__(self):
        self.nodes = []
        self.labels = {}
        self.used_ids = set()

    # ---- primitives -------------------------------------------------
    def line(self, text=None, who=None, e=None, bg=None, ch=None, show=None,
             hide=False, bgm=None, weather=None, fx=None, eff=None,
             ending=None, text_speed=None, choices=None, show2=None, hide2=False):
        nid = "n%03d" % (len(self.nodes) + 1)
        node = {}
        if who:
            node["who"] = who
        if text:
            node["text"] = text
        if e:
            node["e"] = e
        if bg:
            node["bg"] = bg
        if ch:
            node["ch"] = ch
        if show:
            node["show"] = show
        if hide:
            node["hide"] = True
        if show2:
            node["show2"] = show2
        if hide2:
            node["hide2"] = True
        if bgm:
            node["bgm"] = bgm
        if weather:
            node["weather"] = weather
        if fx:
            node["fx"] = fx
        if ending:
            node["ending"] = ending
        if choices:
            node["choices"] = choices
        self.nodes.append({"id": nid, "node": node})
        return nid

    def label(self, name):
        self.labels[name] = "n%03d" % (len(self.nodes) + 1)

    def choice(self, options, prompt=None):
        """Attach choices to the last line node."""
        last = self.nodes[-1]
        last["node"]["choices"] = options
        return last["id"]

    def goto(self, label):
        nid = "n%03d" % (len(self.nodes) + 1)
        self.nodes.append({"id": nid, "node": {"goto": "@" + label}})
        return nid

    def branch(self, rules):
        """rules: list of (cond, label). Last entry should be (None, label)."""
        nid = "n%03d" % (len(self.nodes) + 1)
        self.nodes.append({"id": nid, "node": {"branch": rules}})
        return nid

    # ---- finalize ---------------------------------------------------
    def finish(self):
        out = {}
        nodes = self.nodes
        label_targets = {v: k for k, v in self.labels.items()}

        for i, item in enumerate(nodes):
            n = item["node"]
            if "goto" in n:
                n["next"] = n.pop("goto")
            if "branch" in n:
                n["branch"] = [
                    {"if": c, "next": "@" + t} if c else {"next": "@" + t}
                    for c, t in n["branch"]
                ]
            if "choices" in n:
                for c in n["choices"]:
                    if "to" in c:
                        c["next"] = "@" + c.pop("to")
            # implicit next: the following node
            if ("next" not in n and "choices" not in n and "branch" not in n
                    and "ending" not in n and i + 1 < len(nodes)):
                n["next"] = nodes[i + 1]["id"]

        # resolve @label
        for item in nodes:
            n = item["node"]

            def ref(v):
                if isinstance(v, str) and v.startswith("@"):
                    key = v[1:]
                    if key not in self.labels:
                        raise SystemExit("unknown label: %s" % key)
                    return self.labels[key]
                return v

            if "next" in n:
                n["next"] = ref(n["next"])
            if "branch" in n:
                for b in n["branch"]:
                    b["next"] = ref(b["next"])
            if "choices" in n:
                for c in n["choices"]:
                    c["next"] = ref(c["next"])

        meta = META
        meta["count"] = len(nodes)
        for item in nodes:
            out[item["id"]] = item["node"]
        meta["start"] = nodes[0]["id"]
        meta["labelIndex"] = label_targets
        return {"meta": meta, "nodes": out}


META = {
    "title": "새벽 두 시, 3층 병동",
    "subtitle": "구강악안면외과 병동 실습 5일",
    "heroines": {
        "haram": {"name": "정하람", "role": "병동 4년차 간호사", "color": "#4fb8a8"},
        "serin": {"name": "오세린", "role": "응급실 1년차 간호사", "color": "#ef8f92"},
    },
    "endings": {
        "haram_happy": {
            "no": "01", "label": "HAPPY END", "title": "3층의 아침",
            "desc": "마지막 날의 고백, 그리고 다음 당직. 이 병동의 새벽은 이제 두 사람이 함께 센다.",
        },
        "haram_normal": {
            "no": "02", "label": "NORMAL END", "title": "잘 부탁합니다, 선배님",
            "desc": "말하지 못한 마음은 이름표 아래에 두고. 그래도 같은 복도를 걷는 사람이 생겼다.",
        },
        "serin_happy": {
            "no": "03", "label": "HAPPY END", "title": "야식은 두 그릇",
            "desc": "응급실과 병동, 3층과 1층. 멀어도 매일 밤 같은 시간에 만나기로 했다.",
        },
        "serin_normal": {
            "no": "04", "label": "NORMAL END", "title": "먼저 가는 사람",
            "desc": "2주짜리 야간 지원이 끝났다. 손을 흔드는 그녀 뒤로 응급실 불빛이 켜져 있었다.",
        },
        "true_end": {
            "no": "05", "label": "TRUE END", "title": "우리 모두의 라운드",
            "desc": "로맨스보다 먼저 배운 것. 사람을 지키는 일은 혼자 하는 게 아니라는 것.",
        },
    },
}


def main():
    S = Scene()
    for mod in (s0_prologue, s1_day1, s2_night1, s3_day2, s4_dawn, s5_lastday):
        mod.build(S)
    data = S.finish()
    out = os.path.join(os.path.dirname(__file__), "..", "src", "data", "scenario.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print("wrote", out, len(data["nodes"]), "nodes", len(data["meta"]["endings"]), "endings")


if __name__ == "__main__":
    main()
