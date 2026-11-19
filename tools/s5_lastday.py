# -*- coding: utf-8 -*-
"""4일차 — 마지막 라운드, 그리고 다섯 개의 결말"""


def build(S):
    S.line(bg="ward_day", ch="4일차 · 마지막 라운드", bgm="day", hide=True,
           text="마지막 날. 실습 수첩은 절반이 넘게 찼고, 손글씨가 조금 달라져 있었다.")
    S.line(who="정하람", e="base", show={"id": "haram", "expr": "base"},
           text="3호실 환자분, 오늘 퇴원이에요. 선생님이 퇴원 설명 해 보세요. 제가 옆에 있을게요.")
    S.line(who="나", text="…제가요?")
    S.line(who="정하람", text="네가 제일 많이 봤잖아요. 그 사람 새벽을.")
    S.line(text="3호실. 김우진 님이 휠체어에 앉아 있었다. 붓기는 많이 빠졌고, 얼굴에 처음으로 웃음이 있었다.")
    S.line(who="김우진", text="선생님이 그날 새벽에 계셔서 다행이었어요. 혼자였으면 진짜 무서웠을 거예요.")
    S.line(who="나", text="…제가 한 건 손 잡은 것밖에 없어요.")
    S.line(who="김우진", text="그게 제일 큰 거예요. 아픈 사람한테는.")
    S.line(text="퇴원 설명을 하면서 목소리가 두 번 갈라졌다. 하람 씨가 뒤에서 아무 말도 하지 않고 기다려 주었다.")
    S.line(hide=True, text="점심. 세린이 응급실에서 올라와서, 마지막 야식이라며 봉투를 내려놓았다.")
    S.line(show={"id": "serin", "expr": "base"}, who="오세린", text="선생님, 저 내일부터 응급실 복귀예요. 2주 금방이네요.")
    S.line(who="오세린", text="3층 올라오는 계단 이제 다 외웠는데. 아깝다.")
    S.line(who="나", text="…아깝네요.")
    S.line(who="오세린", e="blush", text="네? 뭐가요?")
    S.line(who="나", text="계단이요. 이제 안 오시잖아요.")
    S.line(who="오세린", e="surprised", text="…")
    S.line(who="오세린", e="blush", text="아, 뭐야. 그런 말 하면 제가 또 올라오잖아요.")
    S.line(who="정하람", text="세린아. 퇴근하고 와. 야식은 그때 사 와.")
    S.line(who="오세린", e="base", text="언니가 그런 말 하면 진짜 와요. 알았어요, 올게요!")

    S.line(bg="rooftop_dusk", ch="마지막 저녁 · 옥상", bgm="warm", hide=True,
           text="마지막 저녁. 옥상. 해가 지고, 도시에 불이 하나씩 켜지기 시작했다.")
    S.line(show={"id": "haram", "expr": "base"}, who="정하람", text="5일이 이렇게 짧아요? 원래 병동은 이렇게 안 짧은데.")
    S.line(who="나", text="…저는 길었어요. 진짜로.")
    S.line(who="정하람", text="길었으면 잘 배운 거예요.")
    S.line(text="세린이 늦게 도착했다. 봉투를 들고, 계단을 세 칸씩. 숨이 차서 말도 제대로 못 했다.")
    S.line(show={"id": "serin", "expr": "base"}, who="오세린", text="야식! 이번엔 김밥이랑… 어, 뭐지. 이거. 아무튼 맛있는 거예요.")
    S.line(text="세 사람이 의자 두 개에 나눠 앉았다. 하람 씨가 가운데, 내가 오른쪽, 세린이 왼쪽.")
    S.line(text="해가 완전히 졌다. 도시 불빛이 하늘 대신 아래에서 켜졌다.")

    S.line(text="마지막 인사를 어떻게 해야 할까. 이 5일 동안, 나는 무엇을 받았나.")
    S.line(text="그 생각만 하다가, 하람 씨가 먼저 입을 열었다.")
    S.line(who="정하람", e="base", text="선생님. 이제 내일부터 안 오시죠.")
    S.line(who="나", text="…네.")
    S.line(who="정하람", text="답을 하나만 들을게요. 이 5일, 어땠어요?")
    S.choice([
        {"t": "하람 씨에게, 5일 동안 나를 지켜 준 사람에게 말한다.", "to": "f_haram",
         "when": {"affMin": {"haram": 6}}},
        {"t": "세린에게, 계단을 오르내린 사람에게 말한다.", "to": "f_serin",
         "when": {"affMin": {"serin": 6}}},
        {"t": "두 사람에게, 이 병동에게 말한다.", "to": "f_all"},
    ])

    # ================= 하람 루트 =================
    S.label("f_haram")
    S.line(show={"id": "haram", "expr": "base"}, who="나",
           text="선배님. 저 그거, 계속 생각했어요. 선배님이 창가에 서 있던 새벽.")
    S.line(who="나", text="제가 거기 있었으면 좋겠다고. 다음에도, 그다음에도.")
    S.line(who="정하람", e="surprised", text="…선생님. 그거, 지금, 무슨 뜻으로.")
    S.line(who="나", text="좋아한다는 뜻으로요.")
    S.line(text="세린이 일부러 소리를 크게 내며 봉투를 정리했다. 하람 씨는 나를 보고, 손을 한 번 쥐었다 폈다 했다.")
    S.choice([
        {"t": "\"선배님, 저 정식으로 다시 말할게요. 좋아해요.\"", "to": "e_haram_happy"},
        {"t": "더 말하지 않고, 웃으면서 자리를 정리한다.", "to": "e_haram_normal"},
    ], prompt="마지막으로")

    S.label("e_haram_happy")
    S.line(who="정하람", e="blush", text="…4년 동안, 이런 말 들은 적 없는데.")
    S.line(who="정하람", text="한 번만 더, 말해 줄래요? 못 들은 것처럼.")
    S.line(who="나", text="좋아해요, 선배님.")
    S.line(who="정하람", e="blush", text="…응.")
    S.line(who="오세린", e="blush", text="아, 저 여기 있어요! 두 사람! 저 여기 있다고요!")
    S.line(who="정하람", text="알아. 그래서 더 부끄러운 거야.")
    S.line(text="셋이 웃었다. 옥상 위에서 웃는 소리는, 이상하게도 아래까지 내려가지 않았다.")
    S.line(who="정하람", e="base", text="선생님. 다음 달 당직표. 제가 손봐 달라고 할까요.")
    S.line(who="나", text="그건 좀 비정규직 갑질인데요.")
    S.line(who="정하람", text="4년차의 특권이에요.")
    S.line(who="정하람", e="blush", text="…그리고, 다음엔 내가 커피 타 줄게요. 그거 하나는 자신 있어요.")
    S.line(text="병동의 새벽은 이제 두 사람이 센다.", ending="haram_happy")

    S.label("e_haram_normal")
    S.line(who="나", text="…선배님, 5일 동안 정말 감사했습니다. 제가 여기서 배운 거, 잊지 않을게요.")
    S.line(who="정하람", e="base", text="네. 나도 선생님한테 배운 게 있어요. 그거, 진짜예요.")
    S.line(who="정하람", text="가끔은요. 사람이 밝은 걸 배우는 게, 어두운 걸 배우는 것보다 오래 걸려요.")
    S.line(text="말하지 못한 것은 이름표 아래에 두고 왔다. 대신 악수를 했다. 아주 정확하게, 두 번 흔들고 놓았다.")
    S.line(who="정하람", e="base", text="그럼, 3층에서 봐요. 선생님.")
    S.line(text="지하철 안에서 손바닥을 몇 번 폈다. 그 온도가 한 정거장쯤 남아 있었다.", ending="haram_normal")

    # ================= 세린 루트 =================
    S.label("f_serin")
    S.line(show={"id": "serin", "expr": "base"}, who="나",
           text="세린아. 나 계속 생각했어. 5층까지 안 올라와도 되는 날에도, 네가 올라올 것 같아서.")
    S.line(who="오세린", e="surprised", text="…네? 그게 무슨.")
    S.line(who="나", text="올라와 줬으면 좋겠어. 계속. 매일 밤.")
    S.line(who="오세린", e="blush", text="…야식 값은요?")
    S.line(who="나", text="내가 낼게.")
    S.line(who="오세린", e="blush", text="…그럼, 그거면 돼요.")
    S.line(text="하람 씨가 조용히 일어나 의자를 하나 더 끌어다 놓고, 그 위에 김밥을 펼쳤다. 아무 일도 없었다는 얼굴로.")
    S.choice([
        {"t": "\"매일 두 시에, 3층에서 기다릴게.\"", "to": "e_serin_happy"},
        {"t": "\"오늘 진짜 고마웠어. 다음에 또 봐.\"", "to": "e_serin_normal"},
    ], prompt="마지막으로")

    S.label("e_serin_happy")
    S.line(who="나", text="매일 두 시에, 3층에서 기다릴게. 응급실이 바쁘면 늦어도 돼. 안 와도 되고.")
    S.line(who="오세린", e="blush", text="그렇게 말하면 무조건 올라와야 되잖아요.")
    S.line(who="오세린", text="알았어요. 두 시. 두 시면 저 아직 안 자요. 원래 응급실에서도 제일 늦까지 깨어 있어요.")
    S.line(who="오세린", e="base", text="대신 언니한테는 3그릇이라고 해 둬요. 저는 1.5로 합니다.")
    S.line(who="정하람", text="들었어.")
    S.line(who="오세린", e="surprised", text="아.")
    S.line(text="병원의 밤이 조금 재미있어졌다. 새벽 두 시가, 기다려지는 시간이 됐다.", ending="serin_happy")

    S.label("e_serin_normal")
    S.line(who="나", text="오늘 진짜 고마웠어. 다음에 또 봐.")
    S.line(who="오세린", e="base", text="네. 다음에 또 봐요, 선생님.")
    S.line(text="세린이 봉투를 정리해서 일어섰다. 가기 전에, 아주 작게 \"진짜 다음에도 봐요?\"라고 말했는데, 바람에 섞여서 잘 안 들렸다.")
    S.line(text="다음 날 계단에서 마주칠 때까지, 그 말을 몇 번이나 되새겼는지 모르겠다.", ending="serin_normal")

    # ================= 모두의 루트 =================
    S.label("f_all")
    S.line(who="나", text="5일 동안, 저는 사람 둘한테 배운 게 있어요. 숫자보다 표정을 먼저 보는 것, 그리고 새벽에 옆에 있어 주는 것.")
    S.line(who="나", text="선배님. 세린아. 함께 있어 줘서 고마웠어요.")
    S.line(who="정하람", e="base", text="선생님, 그거 병원에서 하면 안 된다고 배웠죠?")
    S.line(who="나", text="…네. 아직 안 배웠습니다.")
    S.line(who="오세린", e="base", text="에이, 좋은데요. 이거 좋은데. 저 녹음했다고요.")
    S.line(who="정하람", text="그건 좀.")
    S.line(text="세 사람이 옥상에서 오래 앉아 있었다. 야식은 다 없어졌고, 대신 별이 하나 두 개 보이기 시작했다.")
    S.line(who="정하람", e="base", text="선생님. 하나 더 물어봐도 돼요? 실습 끝나면, 어디 갈 거예요?")
    S.line(who="나", text="…구강악안면외과를 계속 해 보고 싶어요. 여기 병동 순환도 다시 신청할 거고요.")
    S.line(who="정하람", e="surprised", text="여기요? 이 새벽이요?")
    S.line(who="나", text="그 새벽이요.")
    S.line(who="정하람", e="base", text="…그럼, 다시 실습생 이름으로 돌아오는 거잖아요. 또 처음부터 알려 줘야 하는데.")
    S.line(who="오세린", text="그럼 그때 제가 다 알려 줄게요! 저 이제 1년 넘은 사람이에요. 완전 고참.")
    S.line(who="정하람", text="1년이 고참이야.")
    S.line(who="오세린", e="blush", text="응급실 기준으로는요.")
    S.line(text="웃음이 멎은 뒤에도 셋은 한참 그 자리에 앉아 있었다.")
    S.line(text="그날의 새벽은 세 사람이 셌다. 아마 다음 새벽도.", ending="true_end")
