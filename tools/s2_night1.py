# -*- coding: utf-8 -*-
"""1일차 밤 — 첫 당직, 야식, 그리고 새벽 3시"""


def build(S):
    S.line(bg="ward_night", text="라운드. 하람 씨가 문을 반쯤 열고, 불을 켜지 않고, 발소리만 죽여서 들어간다.")
    S.line(who="정하람", text="깨우지 않으면서 보는 거예요. 숨소리, 얼굴색, 이불 위치. 이불이 바닥에 있으면 열이 있는 거예요.")
    S.line(text="따라 다니면서 배운다. 의학보다 먼저 손이 익는다는 걸 알았다.")
    S.line(text="자정이 지나자 복도가 길어졌다. 낮에는 두 걸음이던 거리가, 밤에는 다섯 걸음이다.")
    S.line(show2={"id": "serin", "expr": "base"}, who="오세린", text="선생님! 야식 왔어요!")
    S.line(text="세린이 계단에서 폴짝 뛰어 내려왔다. 손에 봉투 두 개. 하나는 김밥, 하나는… 라면 냄새가 난다.")
    S.line(who="오세린", text="2층에서 라면 끓였어요. 여기선 냄새 퍼지면 안 되니까, 창문 다 닫고 끓였어요. 임무 완수.")
    S.line(who="정하람", e="base", text="응급실에서 왔으면 응급실 냄새부터 빼고 와야지.")
    S.line(who="오세린", e="blush", text="…냄새 나요? 저 지금 라면 냄새만 나는 줄 알았는데.")
    S.line(text="하람 씨가 작게 웃었다. 오늘 처음 보는, 힘을 뺀 웃음.")
    S.line(who="오세린", text="자, 선생님. 첫 당직 기념이요. 세 그릇. 언니도 한 그릇.")
    S.line(who="정하람", text="나는 반 그릇.")
    S.line(who="오세린", text="그럼 제가 1.5.")

    S.choice([
        {"t": "세린 옆에 앉아 라면을 나눈다.", "to": "n1_eat_serin", "eff": {"serin": 2}},
        {"t": "하람 씨 옆자리를 비켜 준다.", "to": "n1_eat_haram", "eff": {"haram": 2}},
        {"t": "\"먼저 3호실 한 번 더 보고 올게요.\"", "to": "n1_round", "eff": {"haram": 1, "flag": "diligent"}},
    ])

    S.label("n1_eat_serin")
    S.line(text="세린 옆에 앉았다. 그녀가 김밥을 반으로 갈라 주면서, 아주 작게 말했다.")
    S.line(who="오세린", e="base", text="저 사실… 오늘 좀 무서웠어요. 응급실에서 올라올 때, 3호실 환자분이 아프다고 해서요.")
    S.line(who="오세린", text="제가 잘못한 건가 싶고. 근데 하람 언니 오면 다 괜찮아질 거 같고.")
    S.line(who="나", text="지금도 충분히 잘했어. 올라와서 바로 말했잖아.")
    S.line(who="오세린", e="blush", text="…그럼 다행이네요. 선생님이 그렇게 말해 주니까, 진짜 다행인 것 같아요.")
    S.line(text="라면이 조금 불었는데, 그게 오히려 맛있었다.")
    S.goto("n1_late")

    S.label("n1_eat_haram")
    S.line(text="하람 씨 옆자리를 비켜 줬다. 그녀가 잠깐 나를 보고, 조용히 앉았다.")
    S.line(who="정하람", e="base", text="라면은 반 그릇이 딱이에요. 밤에 많이 먹으면 새벽에 배가 아파서 못 일어나요.")
    S.line(who="나", text="그런 것까지 계산하세요?")
    S.line(who="정하람", text="4년 하면요. 몸이 먼저 알게 돼요.")
    S.line(text="어깨가 가까웠다. 라면 김에 섞여서, 그녀의 체온이 고스란히 느껴졌다.")
    S.line(who="정하람", e="blush", text="…선생님. 그거 제 젓가락이에요.")
    S.line(who="나", text="아. 죄송합니다.")
    S.line(who="정하람", text="됐어요. 그냥 먹어요. 밤엔 다 그럴 수 있죠.")
    S.goto("n1_late")

    S.label("n1_round")
    S.line(who="나", text="먼저 3호실 한 번 더 보고 올게요.")
    S.line(who="정하람", e="base", text="…네. 그게 맞아요.")
    S.line(text="다녀오니 3호실 환자는 자고 있었다. 이불은 제자리에 있었고, 숨소리는 규칙적이었다.")
    S.line(text="돌아와 보니 세 그릇 중 하나가 뚜껑을 닫은 채 남아 있었다. 하람 씨가 내 몫을 덮어 둔 것이다.")
    S.line(who="정하람", text="식었어요. 그래도 먹어요. 밤엔 식은 것도 맛있어요.")
    S.goto("n1_late")

    S.label("n1_late")
    S.line(hide2=True, text="새벽 2시 40분. 세린이 먼저 아래층으로 내려갔다. 응급실 호출이었다.")
    S.line(hide=True, text="복도 창가. 하람 씨가 혼자 서서 바깥을 보고 있었다. 유리창에 그녀의 얼굴이 겹쳐 비쳤다.")
    S.line(text="무언가 말하고 싶은데, 무엇을 말해야 할지 몰랐다.")
    S.choice([
        {"t": "\"선배님, 괜찮아요?\" 하고 조용히 다가간다.", "to": "n1_three_ask", "eff": {"haram": 2}},
        {"t": "따뜻한 물을 한 잔 따라다가 옆에 둔다.", "to": "n1_three_water", "eff": {"haram": 2}},
        {"t": "부르지 않고 그냥 지나친다.", "to": "n1_three_pass", "eff": {"haram": 0}},
    ])

    S.label("n1_three_ask")
    S.line(who="나", text="선배님. 괜찮아요?")
    S.line(who="정하람", e="surprised", text="…아. 네. 그냥, 창밖이 조용해서.")
    S.line(who="정하람", e="base", text="3년 전에, 저 응급실에 있었어요. 그때 새벽마다 이 창을 봤어요. 여기가 유일하게 조용한 자리였거든요.")
    S.line(who="나", text="지금은요?")
    S.line(who="정하람", text="지금은… 누가 옆에 서 있네요. 그게 좀 다르네요.")
    S.line(text="그 말을 나에게 한 건지, 창밖에 한 건지 알 수 없었다. 다만 두 귀가 뜨거웠다.")
    S.goto("n1_dawn")

    S.label("n1_three_water")
    S.line(text="말을 걸지 않고 물을 한 잔 따라다가, 옆에 조용히 놓았다.")
    S.line(who="정하람", e="surprised", text="…어. 고마워요.")
    S.line(text="그녀가 컵을 들고 한 모금 마셨다. 그리고 아주 작게 웃었다.")
    S.line(who="정하람", e="base", text="이런 거예요. 말 안 하고 챙겨 주는 거. 병동에서 제일 어려운 기술인데, 선생님은 첫날에 하네요.")
    S.line(who="나", text="그냥… 목이 마르실 것 같아서요.")
    S.line(who="정하람", text="그게 기술이에요.")
    S.goto("n1_dawn")

    S.label("n1_three_pass")
    S.line(text="지나치려다, 발이 조금 느려졌다. 하람 씨가 먼저 말을 걸었다.")
    S.line(who="정하람", text="안 자요?")
    S.line(who="나", text="…잠이 안 와서요.")
    S.line(who="정하람", e="base", text="그럴 거예요. 첫 당직은 원래 그래요. 몸은 피곤한데 귀는 안 잠들죠.")
    S.line(who="정하람", text="30분만 누워요. 그게 3시간보다 나아요. 제가 부를게요.")
    S.goto("n1_dawn")

    S.label("n1_dawn")
    S.line(bg="ward_night", text="새벽 5시. 복도 끝에서 첫 햇빛이 들어왔다. 형광등이 서서히 꺼지고, 창문 쪽이 분홍색으로 물들었다.")
    S.line(who="정하람", e="base", text="봐요. 이게 3층 새벽이에요. 여기 앉으면 딱 10분쯤 예뻐요.")
    S.line(text="정말로 예뻤다. 병원 복도가 이렇게 보이는 줄은 몰랐다.")
    S.line(who="정하람", text="10분 지나면 다시 병동이고요.")
    S.line(who="나", text="…선배님은 여기서 몇 번 보셨어요?")
    S.line(who="정하람", e="base", text="세어 봤어요. 작년에 72번. 올해는… 아직 40번쯤?")
    S.line(text="72번. 그 숫자가 왜인지 가슴 한쪽을 눌렀다.")
