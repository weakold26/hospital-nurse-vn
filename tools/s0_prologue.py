# -*- coding: utf-8 -*-
"""프롤로그 — 3층 병동, 첫 아침"""


def build(S):
    S.line(
        text="엘리베이터가 3층에서 멈췄다.\n문이 열리자 소독약 냄새와, 어디선가 끓고 있는 죽 냄새가 한꺼번에 밀려왔다.",
        bg="ward_day", ch="프롤로그 · 첫 아침", bgm="day", fx="dust")
    S.line(text="치과대학 4학년. 병동 실습 마지막 주.\n왼손에는 각이 접힌 실습 수첩, 가슴에는 아직 낯선 이름표.")
    S.line(text="구강악안면외과 3층.\n여기서 닷새를 지내면, 내 병원 실습은 끝난다.")
    S.line(who="나", e=None, text="……늦진 않았지.")
    S.line(text="복도 끝 스테이션. 차트를 정리하던 간호사가 고개를 들었다. 이름표를 한 번 보고, 나를 한 번 보고.")
    S.line(show={"id": "haram", "expr": "base"}, who="정하람",
           text="실습생이죠. 오늘부터 여기 도는 분.")
    S.line(who="정하람", text="정하람이에요. 이 병동 4년째고, 오늘은 제가 인수인계부터 다 붙어서 알려드릴 거예요.")
    S.line(who="정하람", e="base",
           text="수첩에 제 이름부터 적어 두세요. 밤에는 얼굴보다 이름이 먼저거든요.")
    S.line(text="말투가 참 고르다. 다정한데, 한 글자도 낭비가 없다.")
    S.line(who="정하람", text="자, 첫인사부터. 어떤 실습생인지 궁금해서요.", choices=[
        {"t": "수첩을 덮고 두 손으로 인사한다.", "to": "p_greet", "eff": {"haram": 2}},
        {"t": "어색해서 웃기만 한다.", "to": "p_grin", "eff": {"haram": 1}},
        {"t": "먼저 서류부터 정리하겠다고 말한다.", "to": "p_paper", "eff": {"haram": 0}, },
    ])

    S.label("p_greet")
    S.line(who="나", text="안녕하세요. 이번 주 실습 맡게 된 학생입니다. 잘 부탁드립니다.")
    S.line(who="정하람", e="base", text="네. 목소리 좋네요. 병동에서는 그게 은근히 중요해요.")
    S.line(text="칭찬인지 농담인지 애매하게 웃자, 그녀도 짧게 웃었다. 처음 보는 사람인데 어색하지가 않다.")
    S.goto("p_handover")

    S.label("p_grin")
    S.line(text="말이 안 나와서 그냥 웃었다. 하람 씨가 잠깐 나를 보다가, 고개를 끄덕였다.")
    S.line(who="정하람", text="긴장한 거 알겠어요. 괜찮아요. 첫날은 다 그래요. 저도 그랬고.")
    S.goto("p_handover")

    S.label("p_paper")
    S.line(who="나", text="인수인계 자료부터 정리하는 게 좋을 것 같아서요. 어디에 두면 될까요?")
    S.line(who="정하람", e="surprised", text="아, 벌써? …좋은데요.")
    S.line(who="정하람", e="base", text="그런데 순서를 바꿔요. 서류보다 사람이 먼저예요. 여기선.")
    S.line(text="딱 잘라 말하는데도 기분이 상하지 않는다. 그게 이 사람의 기술인 것 같았다.")
    S.goto("p_handover")

    S.label("p_handover")
    S.line(who="정하람", text="3층은 구강악안면외과예요. 턱 수술, 얼굴 뼈 수술, 그다음에 암 수술까지.")
    S.line(who="정하람", text="수술 다음 날이 제일 바빠요. 붓고, 아프고, 밥을 못 먹으니까. 밤에도 계속 깨고요.")
    S.line(who="정하람", text="그래서 여기 당직은 조용할 때가 없어요. 대신…")
    S.line(who="정하람", e="base", text="조용한 새벽엔, 복도가 참 예뻐요. 그건 나중에 보여드릴게요.")
    S.line(text="그 말이 왜인지 오래 남았다.")
    S.line(who="정하람", text="오늘은 낮 근무예요. 저 따라다니면서 눈으로 다 담아 두세요. 손은 제가 시키면 대요.")
    S.line(who="나", text="네, 알겠습니다.")

    # 세린 등장
    S.line(bg="ward_day", fx="none", text="그때, 복도 저편에서 누군가 계단을 두 칸씩 뛰어 올라왔다.")
    S.line(show={"id": "serin", "expr": "base"}, who="오세린",
           text="하람 언니! 3호실 환자분 올라왔어요! 응급실에서요!")
    S.line(who="오세린", text="아, 그리고 이거. 어제 언니가 커피 사 준다 했잖아요. 안 사 주면 제가 사 올게요.")
    S.line(who="정하람", e="base", text="세린아. 환자 인계부터. 커피는 그다음.")
    S.line(who="오세린", e="surprised", text="아아, 네! 죄송합니다!")
    S.line(text="줄줄이 말하다가 딱 멈추는 게, 꽤 귀엽다. 아까운 기세가 아깝다.")
    S.line(who="오세린", e="base", text="…어? 이 분은?")
    S.line(who="정하람", text="이번 주 우리 병동 도는 실습생. 세린인 응급실 1년차인데, 2주 동안 야간 지원 나와 있어요.")
    S.line(who="오세린", e="base", text="아, 그래요? 그럼 우리 밤에 계속 볼 사이네요!")
    S.line(text="눈이 반짝인다. 이런 사람이 응급실에 있으면, 아픈 사람도 조금은 덜 무서울 것 같다.")
    S.choice([
        {"t": "장난스럽게 \"그럼 야식도 챙겨주시는 거죠?\"", "to": "p_serin_joke", "eff": {"serin": 2}},
        {"t": "정식으로 인사를 한다.", "to": "p_serin_formal", "eff": {"serin": 1}},
        {"t": "웃으며 고개만 끄덕인다.", "to": "p_serin_nod", "eff": {"serin": 0}},
    ])

    S.label("p_serin_joke")
    S.line(who="나", text="그럼 야식도 챙겨주시는 거죠?")
    S.line(who="오세린", e="blush", text="뭐야, 벌써부터? …봐서요. 언니한테 물어보고.")
    S.line(who="정하람", text="왜 나한테 물어봐. 네가 사면 되잖아.")
    S.line(who="오세린", e="base", text="에이. 그럼 반반이요. 선생님도 내세요!")
    S.line(text="2주짜리 인연인데, 벌써 반반을 논하고 있다.")
    S.goto("p_serin_end")

    S.label("p_serin_formal")
    S.line(who="나", text="안녕하세요. 이번 주 실습 나온 학생입니다. 잘 부탁드립니다.")
    S.line(who="오세린", e="base", text="네! 잘 부탁해요! 아, 저는 반말 할게요. 그게 편해서. 괜찮죠?")
    S.line(who="나", text="네, 편하신 대로.")
    S.line(who="오세린", text="좋아, 그럼 선생님도 편하게 하세요. 여기선 다 편하게 해요. 언니 빼고.")
    S.line(who="정하람", text="들리는데.")
    S.line(who="오세린", e="surprised", text="앗.")
    S.goto("p_serin_end")

    S.label("p_serin_nod")
    S.line(text="웃으면서 고개를 끄덕였다. 세린이 잠깐 가만히 있다가, 작게 손을 흔들었다.")
    S.line(who="오세린", text="…네. 나중에 봐요, 선생님.")
    S.goto("p_serin_end")

    S.label("p_serin_end")
    S.line(who="오세린", text="그럼 저 내려갈게요! 3호실 환자분, 수술 이틀째고 통증 조절 중이에요. 자세한 건 차트에.")
    S.line(hide=True, text="세린이 계단으로 사라졌다. 발소리가 두 층을 내려가서야 잦아들었다.")
    S.line(who="정하람", e="base", text="저 애, 응급실에서 제일 젊어요. 그래서 제일 많이 뛰어요.")
    S.line(who="정하람", text="…많이 뛰다가 넘어지기도 하고.")
    S.line(text="그 말에는 여러 겹이 있다. 무슨 겹인지는 아직 모르겠다.")
    S.line(who="정하람", text="자, 가요. 회진부터.")
