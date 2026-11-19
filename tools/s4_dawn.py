# -*- coding: utf-8 -*-
"""3일차 새벽 두 시 — 3호실"""


def build(S):
    S.line(bg="ward_night", ch="3일차 · 새벽 두 시", bgm="night", hide=True, fx="none",
           text="3일차. 밤 11시 인수인계가 끝나고, 병동이 다시 잠잠해졌다.")
    S.line(text="세린이 약속대로 라면을 끓여 왔다. 이번엔 계란도 있었다. 하람 씨는 \"반 그릇\"이라더니 이번엔 한 그릇을 다 먹었다.")
    S.line(who="정하람", e="base", show={"id": "haram", "expr": "base"},
           text="선생님. 오늘 밤은 3호실을 잘 봐 주세요. 수술 이틀째에서 사흘째로 넘어가는 밤이 제일 위험해요.")
    S.line(who="정하람", text="붓기가 제일 심하고, 환자분이 제일 지쳐 있고. 밤에 혼자 있으면 더.")
    S.line(who="나", text="알겠습니다.")

    S.line(text="새벽 1시 50분. 3호실에서 작은 소리가 났다. 신음인지, 뭔가 떨어지는 소리인지.")
    S.line(text="복도에는 나 혼자였다. 하람 씨는 2층 약품실, 세린은 5층 지원 중.")
    S.line(text="문을 열었다. 김우진 님이 침상 난간을 붙잡고 앉아 있었다. 입가에 붉은 것이 묻어 있고, 베개에 얼룩이 번져 있었다.")
    S.line(who="김우진", e=None, hide=True, text="…선생님. 피가, 자꾸…")
    S.line(text="수술 부위 출혈. 머릿속이 하얘졌다. 어제 배운 것들이 한꺼번에 떠오르는데, 손이 그걸 따라가지 못했다.")
    S.line(text="지금 필요한 건 두 가지다. 사람을 부르는 것, 그리고 이 사람을 혼자 두지 않는 것.")
    S.choice([
        {"t": "호출 벨을 누르고, 환자분 손을 잡은 채 옆에 앉는다.",
         "to": "d3_arrive_hold", "eff": {"haram": 2, "serin": 2, "flag": "night_patient"}},
        {"t": "하람 씨에게 즉시 전화하고 지시를 받는다.",
         "to": "d3_arrive_call", "eff": {"haram": 2, "flag": "reported"}},
        {"t": "세린을 부르고, 처치 준비를 먼저 한다.",
         "to": "d3_arrive_team", "eff": {"serin": 2, "flag": "team"}},
    ])

    # --- 공통: 하람 도착 ---
    S.label("d3_arrive_hold")
    S.line(who="정하람", e="serious", show={"id": "haram", "expr": "serious"},
           text="비켜 주세요. 소독하고 압박할게요. 선생님은 옆에서 환자분 얼굴 보세요.")
    S.line(who="정하람", text="지금 제일 중요한 건 환자분이 숨을 편하게 쉬는 거예요. 말 걸어 주세요. 계속.")
    S.line(who="나", text="우진 님. 저 여기 있어요. 제가 여기 있을게요. 괜찮아요, 괜찮아질 거예요.")
    S.line(text="내 목소리가 떨렸다. 그런데도 환자분이 내 손을 꽉 잡았다. 아픈 사람이 나를 붙잡고 있었다.")
    S.line(who="정하람", text="좋아요. 그대로. 5분만 더.")
    S.goto("d3_after")

    S.label("d3_arrive_call")
    S.line(text="전화를 걸었다. 두 번 울리고 받았다.")
    S.line(who="정하람", text="말해요.")
    S.line(who="나", text="3호실 출혈입니다. 환자분 앉아 계시고, 베개에 혈흔 있어요.")
    S.line(who="정하람", text="소독솜이랑 압박 거즈 준비하고, 환자분 눕히지 말고 상체 올린 채로. 지금 올라갈게요. 30초.")
    S.line(text="30초를 셌다. 손은 시키는 대로 움직였고, 머리는 조용해졌다. 누가 정해 주면, 이렇게까지 해낼 수 있다는 게 신기했다.")
    S.goto("d3_after")

    S.label("d3_arrive_team")
    S.line(text="세린을 불렀다. 계단을 세 칸씩 올라오는 소리가 났다.")
    S.line(who="오세린", e="serious", show={"id": "serin", "expr": "serious"},
           text="선생님, 소독솜 제가 잡을게요. 언니한테 연락하셨어요?")
    S.line(who="나", text="지금 한다.")
    S.line(text="세린이 손을 씻고 장갑을 끼는 동안, 나는 하람 씨에게 전화를 걸었다. 목소리가 하나 더 붙으니, 손이 덜 떨렸다.")
    S.goto("d3_after")

    S.label("d3_after")
    S.line(hide=True, text="출혈은 20분 만에 멈췄다. 하람 씨가 처치를 마치고, 아주 낮게 말했다.")
    S.line(who="정하람", e="serious", show={"id": "haram", "expr": "serious"},
           text="선생님. 지금 잘하셨어요. 진짜로.")
    S.line(who="정하람", text="그런데 이제부터가 더 중요해요. 이 사람이 왜 새벽에 출혈했는지, 우리가 뭘 놓쳤는지.")
    S.line(text="칭찬과 채찍이 한 문장 안에 있었다. 그게 이 사람의 방식이다.")

    S.line(bg="ward_night", text="새벽 3시. 처치가 끝나고, 3호실 불이 다시 꺼졌다. 보호자 없이 혼자 온 환자라, 하람 씨가 의자를 침상 옆으로 옮겨 놓았다.")
    S.line(who="오세린", e="base", show2={"id": "serin", "expr": "base"},
           text="선생님. 손 아직 떨려요?")
    S.line(who="나", text="…조금.")
    S.line(who="오세린", text="저도요. 이거 마시면 좀 나아요. 2층 자판기 코코아인데, 오늘은 좀 진해요. 제가 진하게 눌렀거든요.")
    S.line(text="코코아를 받았다. 손바닥이 따뜻했다. 세린이 내 손을 한 번 보고, 아무것도 아닌 척 옆에 앉았다.")
    S.line(who="오세린", e="base", text="있잖아요. 제가 응급실에서 제일 무서운 게 뭔지 알아요?")
    S.line(who="나", text="뭐요?")
    S.line(who="오세린", text="조용해지는 거요. 시끄러울 땐 괜찮아요. 다들 뛰니까. 근데 갑자기 조용해지면, 그게 제일 무서워요.")
    S.line(who="오세린", text="선생님은요?")
    S.choice([
        {"t": "\"나도 조용한 게 무서워요. 그래서 지금 옆에 있어 주는 게 고마워요.\"",
         "to": "d3_cocoa_serin", "eff": {"serin": 3}},
        {"t": "\"나는… 누가 나를 안 부를까 봐 무서워요.\"",
         "to": "d3_cocoa_self", "eff": {"serin": 2, "haram": 1}},
        {"t": "\"모르겠어요. 아직 내가 뭘 무서워하는지 모르겠어요.\"",
         "to": "d3_cocoa_honest", "eff": {"serin": 1, "haram": 1}},
    ])

    S.label("d3_cocoa_serin")
    S.line(who="나", text="나도 조용한 게 무서워요. 그래서 지금 옆에 있어 주는 게 고마워요.")
    S.line(who="오세린", e="blush", text="…아. 그거, 반칙이에요. 그런 말은.")
    S.line(who="오세린", text="저 원래 이런 말에 강한 사람인데. 오늘은 왜 이러지.")
    S.line(text="코코아 컵을 두 손으로 감싸고, 한참 아무 말도 하지 않았다. 그 침묵은 무섭지 않았다.")
    S.goto("d3_end")

    S.label("d3_cocoa_self")
    S.line(who="나", text="나는… 누가 나를 안 부를까 봐 무서워요. 아무 일도 안 하고 있는데, 나만 모르고 있는 그런 거.")
    S.line(who="오세린", e="serious", text="아, 그거 알아요. 완전 알아요.")
    S.line(who="오세린", e="base", text="그래서 제가 이렇게 자주 올라와요. 부르는 소리 말고, 그냥 얼굴이라도 보여 주려고.")
    S.line(text="그 말이 오래 남았다. 응급실에서 5층까지, 계단을 몇 번이나 오른 걸까.")
    S.goto("d3_end")

    S.label("d3_cocoa_honest")
    S.line(who="나", text="모르겠어요. 아직 내가 뭘 무서워하는지도 모르겠어요.")
    S.line(who="오세린", e="base", text="그것도 괜찮아요. 저는 3개월 걸렸어요. 그것도 알게 된 게요.")
    S.line(who="오세린", text="알게 되면 알려 주세요. 제가 기억해 둘게요.")
    S.goto("d3_end")

    S.label("d3_end")
    S.line(hide2=True, show={"id": "haram", "expr": "base"}, text="새벽 4시 반. 세린이 아래층으로 내려갔다. 복도 창가에 하람 씨가 또 서 있었다. 오늘은 내가 먼저 갔다.")
    S.line(who="정하람", e="base", show={"id": "haram", "expr": "base"}, text="안 자요?")
    S.line(who="나", text="선배님도요.")
    S.line(who="정하람", text="나는 이제 습관이에요. 자면 누가 바꿔 주나.")
    S.line(text="그녀가 컵을 내밀었다. 아까 내가 타 준 커피잔과 같은 잔이었다.")
    S.line(who="정하람", text="오늘 새벽, 선생님 목소리 들었어요. 3호실에서.")
    S.line(who="정하람", text="환자분한테 \"제가 여기 있을게요\"라고 했죠. 그거, 제가 4년 전에 처음 배운 말이에요.")
    S.line(who="나", text="…선배님이 하시는 걸 들은 거예요.")
    S.line(who="정하람", e="blush", text="그럼 내 말이 옮은 거네요. 그거면 됐어요.")
    S.line(text="새벽 복도가 조용했다. 무섭지 않은 조용함이었다. 옆에 사람이 있으면, 이 소리도 견딜 만하다는 걸 알았다.")
