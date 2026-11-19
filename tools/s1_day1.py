# -*- coding: utf-8 -*-
"""1일차 낮 — 회진, 그리고 실수"""


def build(S):
    S.line(text="회진은 생각보다 조용했다.\n교수님은 말이 짧았고, 하람 씨는 그 짧은 말 사이를 정확하게 채웠다.")
    S.line(who="정하람", text="3호실 김우진 님, 어제 악교정 수술 이틀째. 부기 최고조예요. 밤에 두 번 깨셨어요.")
    S.line(who="정하람", text="진통제는 여섯 시간마다. 그 사이에 얼음찜질. 지금은 자고 계세요.")
    S.line(text="수첩에 적으려는데 손이 먼저 움직였다. 하람 씨가 그걸 보고 작게 웃었다.")
    S.line(who="정하람", e="base", text="필기 빠르네요. 그거 오늘 진짜 쓸 거예요.")

    S.line(bg="ward_day", text="문제는 7호실에서 생겼다.")
    S.line(text="드레싱을 돕던 중, 나는 침상 옆에 놓인 이름표를 보고 환자분께 말을 걸었다.")
    S.line(who="나", text="서○자 어머님, 잠시만 상체 좀 일으켜 드릴게요.")
    S.line(text="잠깐의 정적. 옆 침상에서 손을 들던 보호자가 나를 봤다.")
    S.line(who="보호자", text="아니, 저희 어머니는 저쪽인데요.")
    S.line(text="얼굴이 확 달아올랐다. 이름표 두 개가 나란히 붙어 있었고, 나는 왼쪽 걸 읽고 오른쪽 환자에게 말을 걸었다.")
    S.line(who="정하람", e="serious", text="잠깐.")
    S.line(who="정하람", text="죄송합니다, 어머님. 저희가 자리를 바꿔서 헷갈렸어요. 제가 다시 확인하고 올게요.")
    S.line(text="그녀가 자연스럽게 그 자리를 가져갔다. 사과도, 변명도 내 몫이 아니게 만들어 버렸다.")
    S.line(hide=True, text="커튼 밖. 하람 씨가 나를 보고 섰다. 무섭게가 아니라, 아주 정확하게.")
    S.line(show={"id": "haram", "expr": "serious"}, who="정하람", text="지금 무슨 일이 일어났는지 알아요?")
    S.choice([
        {"t": "\"확인을 안 하고 이름표만 믿었습니다.\"", "to": "d1_own", "eff": {"haram": 2}},
        {"t": "\"죄송합니다. 다음엔 조심하겠습니다.\"", "to": "d1_sorry", "eff": {"haram": 1}},
        {"t": "아무 말 없이 고개를 숙인다.", "to": "d1_silent", "eff": {"haram": 0}},
    ])

    S.label("d1_own")
    S.line(who="나", text="확인을 안 했습니다. 이름표만 보고, 환자분 얼굴은 안 봤어요.")
    S.line(who="정하람", e="base", text="…네. 그게 정확해요.")
    S.line(who="정하람", text="여기서 제일 위험한 게 그거예요. 잘못 알아도 모르고 넘어가는 것.")
    S.line(who="정하람", e="base", text="좋아요. 오늘 한 번 틀렸으니까, 이제 이 병동 환자 이름은 다 외울 때까지 물어보세요. 스무 번도 물어보세요.")
    S.line(text="칭찬보다 그 말이 더 오래 남았다.")
    S.goto("d1_teach")

    S.label("d1_sorry")
    S.line(who="나", text="죄송합니다. 다음엔 조심하겠습니다.")
    S.line(who="정하람", e="base", text="조심한다는 말은 안 들려요. 그다음에 뭘 할 건지를 들려주세요.")
    S.line(who="나", text="…확인할 때까지 환자분께 한 번 더 여쭙겠습니다.")
    S.line(who="정하람", text="네. 그거면 돼요.")
    S.goto("d1_teach")

    S.label("d1_silent")
    S.line(text="고개만 숙였다. 하람 씨가 잠깐 기다리다가, 한숨처럼 말했다.")
    S.line(who="정하람", text="대답을 안 하면 제가 뭘 가르쳐야 할지 모르겠어요. 저는 선생님 속을 못 읽어요.")
    S.line(who="정하람", e="base", text="틀린 건 괜찮아요. 안 말하는 게 문제예요. 여기서는.")
    S.goto("d1_teach")

    S.label("d1_teach")
    S.line(who="정하람", text="환자한테 이름을 한 번 더 묻는 거, 귀찮아 보이죠?")
    S.line(who="정하람", text="근데 그게 그 사람이 여기 있다는 표시예요. 이름이 불리는 동안은, 아직 사람인 거니까.")
    S.line(text="복도가 조용해졌다. 멀리서 수레바퀴 소리 하나.")
    S.line(who="정하람", e="base", text="…무겁게 들었죠. 미안해요. 첫날에 이런 얘기까지.")
    S.line(who="나", text="아뇨. 들을 만했어요.")
    S.line(who="정하람", text="거짓말 안 하고 다행이다.")

    S.line(bg="ward_day", text="점심. 하람 씨는 차트를 놓지 않았고, 나는 세린에게 끌려 내려왔다.")
    S.line(show={"id": "serin", "expr": "base"}, who="오세린", text="선생님, 편의점 김밥이요. 여기 삼각김밥은 맛없어요. 진짜로.")
    S.line(who="나", text="응급실은 안 바빠?")
    S.line(who="오세린", e="base", text="바빠요. 그래서 지금 먹어요. 안 먹으면 밤에 못 먹어요.")
    S.line(who="오세린", text="아, 그런데 오늘 밤부터 당직이죠? 하람 언니랑 같이?")
    S.line(who="나", text="응. 첫 당직.")
    S.line(who="오세린", e="base", text="그럼 제가 살게요. 첫 당직 기념. …아, 이거 제가 사는 거 처음이네요. 좀 떨리는데.")
    S.choice([
        {"t": "\"그럼 다음엔 내가 살게.\"", "to": "d1_lunch_b", "eff": {"serin": 2}},
        {"t": "\"고맙다. 잘 먹을게.\"", "to": "d1_lunch_c", "eff": {"serin": 1}},
        {"t": "\"돈은 각자 내자.\"", "to": "d1_lunch_a", "eff": {"serin": 0}},
    ])

    S.label("d1_lunch_b")
    S.line(who="나", text="그럼 다음엔 내가 살게. 야식으로.")
    S.line(who="오세린", e="blush", text="…오, 다음이 있네요? 좋아요. 그럼 오늘 밤이 첫 번째고, 내일이 두 번째.")
    S.line(text="손가락으로 브이를 두 개 만든다. 이 사람은 약속을 셀 줄 안다.")
    S.goto("d1_lunch_end")

    S.label("d1_lunch_c")
    S.line(who="나", text="고맙다. 잘 먹을게.")
    S.line(who="오세린", e="base", text="네! 맛없으면 말해요. 그럼 다음엔 다른 거 사 올게요.")
    S.goto("d1_lunch_end")

    S.label("d1_lunch_a")
    S.line(who="나", text="그냥 각자 내자. 내가 오히려 미안해.")
    S.line(who="오세린", e="base", text="에이, 셈이 확실하네요. 좋아요, 그럼 각자.")
    S.line(text="웃긴 했는데, 웃음이 조금 짧았다.")
    S.goto("d1_lunch_end")

    S.label("d1_lunch_end")
    S.line(text="김밥을 먹으면서 창밖을 봤다. 병원 마당의 은행나무가 노랗게 물들어 있었다.")
    S.line(who="오세린", text="선생님은 왜 치대 왔어요?")
    S.line(who="나", text="…손으로 뭔가 고치는 게 좋아서. 그런데 여기 오니까, 고치는 것보다 지키는 걸 더 많이 배우네.")
    S.line(who="오세린", e="base", text="오. 그거 좋은 말이에요. 저 메모할래요.")
    S.line(who="나", text="하지 마.")
    S.line(who="오세린", text="늦었어요. 벌써 적었어요.")

    S.line(bg="ward_day", ch="1일차 · 밤", bgm="night",
           text="저녁 7시. 낮 근무자들이 하나둘 돌아가고, 복도 불빛이 한 단계 내려앉았다.")
    S.line(who="정하람", e="base", text="당직은 두 명이에요. 저, 그리고 선생님. 응급실에서 세린이 지원 나오고요.")
    S.line(who="정하람", text="밤에는 결정을 빨리 해야 할 때가 있어요. 그런데 그 전에, 결정을 누구에게 물을지부터 정하는 거예요.")
    S.line(who="정하람", text="제가 안 보이면 일단 부르세요. 하루 종일 들어요. 그거 하나는 자신 있어요.")
    S.line(text="농담인데 표정은 진지하다. 그래서 더 웃기다.")
    S.line(who="정하람", e="base", text="자, 첫 커피. 이거 마시면 진짜 시작이에요.", choices=[
        {"t": "먼저 하람 씨 잔을 타 드린다.", "to": "d1_coffee_haram", "eff": {"haram": 2}},
        {"t": "세린 몫까지 세 잔을 탄다.", "to": "d1_coffee_three", "eff": {"serin": 2}},
        {"t": "한 잔만 타서 수첩을 펴 든다.", "to": "d1_coffee_study", "eff": {"haram": 1}, "flag": "studious"},
    ])

    S.label("d1_coffee_haram")
    S.line(text="먼저 하람 씨 잔을 채워 건넸다. 그녀가 잠깐 컵을 보다가, 두 손으로 받았다.")
    S.line(who="정하람", e="blush", text="…어, 고마워요. 이런 거 받아본 게 언제인지.")
    S.line(who="나", text="당연한 거죠.")
    S.line(who="정하람", e="base", text="당연한 걸 당연하게 하는 사람이 드물어요. 여기선.")
    S.goto("d1_night_start")

    S.label("d1_coffee_three")
    S.line(text="세 잔을 탔다. 하나는 하람 씨, 하나는 내 것, 하나는 세린 자리에 놓아 두었다.")
    S.line(who="정하람", text="세린이 온 걸 어떻게 알아요?")
    S.line(who="나", text="곧 올 것 같아서요. 아까부터 복도에서 발소리가 들려요.")
    S.line(who="정하람", e="base", text="…선생님, 관찰력 있네요. 수첩에 그거 적어 두세요. 오늘의 발견.")
    S.goto("d1_night_start")

    S.label("d1_coffee_study")
    S.line(text="내 잔만 타서 수첩을 폈다. 하람 씨가 컵을 들고 옆에 서서 내 수첩을 봤다.")
    S.line(who="정하람", text="수액 속도 계산, 그거 맞게 적었네요. 한 번 더 확인해 보세요. 소수점 하나가 밤을 바꿔요.")
    S.line(who="나", text="…네. 한 번 더 볼게요.")
    S.line(who="정하람", e="base", text="좋아요. 밤에 조용한 사람이 제일 무섭거든요. 뭘 하는지 알아야 하니까.")
    S.goto("d1_night_start")

    S.label("d1_night_start")
    S.line(text="밤 11시. 병동은 낮과 다른 소리로 채워졌다. 모니터의 규칙적인 삐, 멀리서 들리는 기침, 문이 닫히는 소리.")
    S.line(who="정하람", text="3호실부터 한 바퀴 돌아요. 표정 보는 게 제일 중요해요. 숫자보다 먼저.")
