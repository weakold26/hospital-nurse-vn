# -*- coding: utf-8 -*-
"""2일차 — 옥상 정원"""


def build(S):
    S.line(bg="ward_day", ch="2일차 · 옥상", bgm="day", hide=True,
           text="2일차 낮. 어제보다 손이 조금 덜 떨렸다. 환자분께 이름을 묻는 것도, 세 번은 자연스러웠다.")
    S.line(who="정하람", e="base", show={"id": "haram", "expr": "base"},
           text="오늘은 드레싱 두 개, 퇴원 설명 하나. 그다음에 외래 도와주고요.")
    S.line(who="정하람", text="아, 그리고 7호실 어머님이 선생님 이름을 물어보시더라고요. 어제 그 실수한 분.")
    S.line(who="나", text="…혼나러 가야 하나요.")
    S.line(who="정하람", e="base", text="칭찬이래요. 오늘 아침에 인사도 먼저 하시고. \"이름 다시 물어봐 줘서 고맙다\"고.")
    S.line(text="그 말에 어제의 창피가 조금 이상하게, 따뜻하게 바뀌었다.")

    S.line(text="저녁 6시. 하람 씨가 옥상 문을 열었다. 병원 건물 사이로 하늘이 크게 열려 있었다.")
    S.line(bg="rooftop_dusk", bgm="warm", weather="clear",
           text="병원 옥상 정원. 넝쿨이 오른 철망, 낡은 의자 두 개, 그리고 도시 위로 지는 해.")
    S.line(who="정하람", e="base", text="여기 사람 별로 안 와요. 아는 사람만 와요.")
    S.line(who="나", text="그럼 저는 아는 사람이 된 거네요.")
    S.line(who="정하람", e="blush", text="…그렇네요. 벌써.")
    S.line(text="바람이 불었다. 그녀의 머리카락이 목덜미에서 살짝 들렸다 내렸다.")

    S.line(who="정하람", text="선생님한테 물어보고 싶은 게 있어요. 왜 이걸 하려고 해요? 치과.") 
    S.line(who="나", text="…사람이 무서워하지 않게 해 주는 일이라서요. 치과는 무서운 데잖아요.")
    S.line(who="정하람", e="base", text="맞아요. 사람들이 제일 무서워하는 두 곳이 치과랑 병원인데, 선생님은 둘 다 하려는 거네요.")
    S.line(who="나", text="그러니까 제가 지금 제일 무서운 사람이죠.")
    S.line(who="정하람", text="하.")
    S.line(text="처음으로 크게 웃었다. 눈이 접혔다. 그 얼굴을 한참 봤다.")
    S.line(who="정하람", e="base", text="…저는요. 3년 전에 응급실에서, 제가 못 지킨 사람이 있어요.")
    S.line(who="정하람", text="그날 이후로 한 달은 아무 말도 못 했어요. 그때 저를 병동으로 옮겨 준 게 선배였고, 그래서 지금 여기 있어요.")
    S.line(who="정하람", text="사람이 사람을 견디게 하는 일. 저는 그걸 배우고 싶어서 계속 여기 있어요.")
    S.line(text="해가 절반쯤 넘어갔다. 그녀의 옆얼굴에 주황색이 얇게 앉았다.")
    S.choice([
        {"t": "\"그 사람을 못 지킨 게 아니라, 그 뒤로 많은 사람을 지키셨잖아요.\"",
         "to": "d2_deep", "eff": {"haram": 3, "flag": "haram_deep"}},
        {"t": "\"저도 그런 사람이 되고 싶어요.\"", "to": "d2_admire", "eff": {"haram": 2}},
        {"t": "아무 말 없이 옆에 서 있는다.", "to": "d2_quiet", "eff": {"haram": 1}},
    ])

    S.label("d2_deep")
    S.line(who="나", text="못 지킨 사람 하나가 아니라, 그 뒤로 지킨 사람을 세 보세요. 그게 선배님이 하시는 일이에요.")
    S.line(who="정하람", e="surprised", text="…")
    S.line(text="그녀가 한참 나를 봤다. 바람 소리가 유난히 컸다.")
    S.line(who="정하람", e="blush", text="선생님, 그런 말은… 아무한테나 하지 마세요.")
    S.line(who="나", text="왜요?")
    S.line(who="정하람", text="…새겨져요. 오래.")
    S.goto("d2_serin")

    S.label("d2_admire")
    S.line(who="나", text="저도 그런 사람이 되고 싶어요. 사람이 견딜 수 있게 해 주는 사람.")
    S.line(who="정하람", e="base", text="그럼 오늘부터 연습하세요. 지금 여기서. 저한테.")
    S.line(who="나", text="…지금요?")
    S.line(who="정하람", e="blush", text="농담이에요. 반은.")
    S.goto("d2_serin")

    S.label("d2_quiet")
    S.line(text="말을 고르다가, 그냥 옆에 서 있었다. 대신 조금 더 가까이.")
    S.line(who="정하람", text="말 안 해도 되는 거 알아요. 그런데 옆에 있어 주는 건, 말보다 어려운 거예요.")
    S.line(text="그녀가 팔을 살짝 내밀어 내 팔에 부딪혔다. 아주 짧게. 그리고는 아무 일도 없던 것처럼 하늘을 봤다.")
    S.goto("d2_serin")

    S.label("d2_serin")
    S.line(show2={"id": "serin", "expr": "serious"}, who="오세린", text="…언니. 선생님.")
    S.line(text="문가에 세린이 서 있었다. 언제부터 있었는지 모른다. 눈이 조금 젖어 있었다.")
    S.line(who="오세린", e="serious", text="저, 잠깐만 있어도 돼요?")
    S.line(who="정하람", text="들어와. 여기 앉아.")
    S.line(show={"id": "serin", "expr": "serious"}, show2={"id": "haram", "expr": "base"}, text="세린이 의자에 앉자, 하람 씨가 내 자리를 비켜 주고 뒤로 물러섰다. 오늘은 세린 차례인 것 같았다.")
    S.line(who="오세린", e="serious", text="저 오늘 응급실에서 혼났어요. 환자분한테 \"괜찮아요\"만 세 번 말했대요. 아무것도 안 하고.")
    S.line(who="오세린", text="근데 저 진짜 열심히 했거든요. 손이 떨려서 그런 거였는데. 그게 말이 안 되잖아요.")
    S.line(text="제일 밝은 사람이 우는 건, 익숙하지가 않다.")
    S.choice([
        {"t": "\"그럼 이제 말 대신 손을 쓰면 되죠. 제가 옆에서 배울게요.\"", "to": "d2_serin_hand", "eff": {"serin": 3, "flag": "serin_deep"}},
        {"t": "\"괜찮아요\" 대신 다른 말을 같이 찾아본다.", "to": "d2_serin_words", "eff": {"serin": 2}},
        {"t": "하람 씨를 부른다.", "to": "d2_serin_haram", "eff": {"haram": 1, "serin": 1}},
    ])

    S.label("d2_serin_hand")
    S.line(who="나", text="말 대신 손을 쓰면 되죠. 다음에 응급실 갈 일 있으면, 제가 옆에서 배울게요.")
    S.line(who="오세린", e="surprised", text="…선생님이요? 응급실에요?")
    S.line(who="나", text="네가 가르쳐 주면 되잖아. 선배처럼.")
    S.line(text="세린이 눈을 크게 떴다. 그리고 웃으려다 실패해서, 코를 훌쩍였다.")
    S.line(who="오세린", e="blush", text="…선배라니. 좋다, 그거. 나 선배다.")
    S.line(text="해가 거의 넘어갔다. 옥상이 한 번에 어두워지고, 셋의 그림자가 길게 늘어졌다.")
    S.goto("d2_end")

    S.label("d2_serin_words")
    S.line(who="나", text="\"괜찮다\"는 말 말고, 다른 말을 같이 찾아보자. 대신 쓸 수 있는 말.")
    S.line(who="오세린", e="serious", text="…뭐가 있어요?")
    S.line(who="나", text="\"제가 여기 있을게요.\" 같은 거.")
    S.line(who="오세린", text="…그거 좋네요. 그거, 진짜 좋네요.")
    S.line(text="세린이 그 말을 두 번 중얼거렸다. 외우는 사람의 입 모양이었다.")
    S.goto("d2_end")

    S.label("d2_serin_haram")
    S.line(who="나", text="선배님. 세린이한테 한마디 해 주세요.")
    S.line(who="정하람", e="base", text="…세린아. 나도 그 소리 들었어. 4년차인데도.")
    S.line(who="오세린", e="surprised", text="언니도요?")
    S.line(who="정하람", text="응. 작년에. 그런데 그 말을 하는 사람은, 대개 밖에서 보고 하는 거야. 안에 있는 사람은 못 해.")
    S.line(who="오세린", e="base", text="…그럼 저 잘하고 있는 거네요.")
    S.line(who="정하람", text="그럼.")
    S.goto("d2_end")

    S.label("d2_end")
    S.line(text="옥상 문을 닫고 내려오는 계단. 세린이 앞, 하람 씨가 뒤, 내가 그 사이.")
    S.line(who="오세린", text="선생님, 내일 새벽에 제가 라면 또 끓여 올게요. 이번엔 계란도 넣어서.")
    S.line(who="정하람", text="이번엔 창문 닫고 끓여.")
    S.line(who="오세린", e="base", text="당연하죠! 이번엔 냄새 안 나게, 냄새만 다른 데로 보내는 방법을 쓸 거예요.")
    S.line(who="정하람", text="그게 되면 너 간호사 그만둬라.")
    S.line(text="계단에서 셋이 같이 웃었다. 병원 계단에서 이렇게 웃어도 되는 건지 모르겠는데, 웃음은 멈추지 않았다.")
