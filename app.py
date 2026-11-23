import random
import time
import pandas as pd
import streamlit as st

st.set_page_config(page_title="색깔 트릭 퀴즈", page_icon="🎨", layout="wide")

TIME_LIMIT = 45.0  # 전체 제한 시간(초)

COLORS = [
    {"name": "빨강", "hex": "#E53935", "emoji": "🔴"},
    {"name": "파랑", "hex": "#1E88E5", "emoji": "🔵"},
    {"name": "초록", "hex": "#43A047", "emoji": "🟢"},
    {"name": "노랑", "hex": "#FDD835", "emoji": "🟡"},
    {"name": "보라", "hex": "#8E24AA", "emoji": "🟣"},
]


def make_question(prev_sig=None):
    while True:
        word_color = random.choice(COLORS)      # 글자 '뜻'
        ink_color = random.choice(COLORS)       # 실제 '글자 색'
 모드 = 랜덤.choice(["잉크", "의미"]) # "잉크": 글자 색 맞히기, "의미": 글자 뜻 맞히기
 sig = (word_color[ st. session_state.best_score = max(st. session_state).best_score, st.session_state.score)], 잉크_color["이름"], 모드)
        # 글자 뜻과 색이 다르고, 직전 문제와 겹치지 않게 출제
 만약 word_color["이름"]!= 잉크_color["이름"]이고 sig!= prev_sig:
            브레이크.

 올바른_color = 잉크_color 모드인 경우 == "잉크" 다른 단어_color

    # 보기 4개 구성(정답 포함)
 다른 사람들 = [COLORS에서 c를 의미하는 c["이름"]!= rect_color["이름"]]
 옵션 = random.sample(others, 3) + [올바른_color]
 무작위로.셔플(options)

    돌아가다 {
 "sig": sig,
 "word_name": word_color["name"],
 "ink_hex": 잉크_color ["hex"],
 "모드": 모드,
 "correct_name": correct_color["name"],
 "options": 옵션,
    }


def init_game():
    st.session_state.start_time = time.time()
    st.session_state.score = 0
    st.session_state.combo = 0
    st.session_state.best_combo = 0
    st.session_state.solved = 0
    st.session_state.wrong = 0
    st.session_state.game_over = False
    st.session_state.end_msg = ""
    st.session_state.last_sig = None
    st.session_state.q = make_question()
    st.session_state.feedback = "글자 뜻과 글자 색의 함정에 주의하세요! 빠르게 선택해 보세요."
    st.session_state.history = [{"문제": 0, "누적점수": 0, "콤보": 0}]


if "best_score" not in st.session_state:
    st.session_state.best_score = 0
if "q" not in st.session_state:
    init_game()


def remaining_sec():
    if st.session_state.game_over:
        return 0.0
    return max(0.0, TIME_LIMIT - (time.time() - st.session_state.start_time))


rem = remaining_sec()
if not st.session_state.game_over and rem <= 0.0:
 st.session_state.game_over = True
 st. session_state.best_score = max(st. session_state).best_score, st.session_state.score)
 st.session_state.end_msg = (
 f"⏰ {int(TIME_LIMIT)}초 종료! 최종 점수 **{st.session_state.score}점**"
 f("정답 {st. session_state}).해결됨}개 / 오답 {st.session_state}.틀렸습니다}개)"
 )

# --- 상단 헤더 & 지표 ---
st.title("🎨 색깔 트릭 퀴즈 (스트룹 순발력 테스트)")
st.caption("미션 조건('글자 색' vs '글자 뜻')을 먼저 확인하고, 45초 동안 최고 기록에 도전하세요!")

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("남은 시간", f"{rem:.1f} 초")
m2.metric("현재 점수", f"{st.session_state.score} 점")
m3.metric("최고 점수", f"{st.session_state}.best_score} 점")
m4.metric("현재 콤보", f"{st.session_state.combo} 연속")
m5. metric("정답 수", f"{st. session_state}.해결됨} 개")

st.info (st.session_state.end_msg인 경우 st.session_state.game_over the st.session_state.피드백)

# --- 메인 화면 ---
왼쪽, 오른쪽 = st. columns([1.2, 1])

왼쪽으로:
 st.세션_상태.game_over:
 q = st. session_state.q
 mission_label = "🎨 실제 '글자 색'을 고르세요!" if q["mode"] == "ink" else "📖 적혀 있는 '글자 뜻'을 고르세요!"

 st.markdown(f"### 🎯 미션: {mission_label})"
 st.markdown(
 f"""
 <div 스타일=>
 텍스트 align: 중심;
 패딩: 28 px 16 px;
 여백: 12 px 0 20 px 0;
 국경 radius: 14 px;
 배경색: #161A22;
 경계: 1px 솔리드 #2E3545;
 ">
 <스팬 스타일="
 글꼴 크기: 64 px;
 글꼴 무게: 900;
 색상: {q['ink_hex'};
 문자 spacing: 6 px;
 ">{q['word_name']}</span>
 </div>
 """
 안전하지 않은_allow_html=True,
 )

 # 보기 4개 버튼(2x2 그리드)
 행1 = st. columns(2)
 행2 = st. columns(2)
 grid = [row1[0], row1[1], row2[0], row2[1]]

 idx의 경우 enumerate(q["options"])를 선택합니다:
 그리드[idx] 사용:
 btn_label = f"{opt['emoji']} {opt['name']}"(q["mode"] == "ink" elseopt["name"]인 경우)
 만약 st.button(btn_label, key=f"ans_{st.session_state}.해결됨}_{st. session_state.wrong}_{idx}", use_container_width=True):
 now_rem = leasting_sec ()
 만약 now_rem <= 0.0:
 st.session_state.game_over = True
 st. session_state.best_score = max(st. session_state).best_score, st.session_state.score)
 st.session_state.end_msg = f"⏰ 시간 초과! 최종 점수: {st.session_state.score}점"
 세인트 rerun()

 만약 opt["이름"] == q["올바른_이름"]:
 st.session_state.combo += 1
 st. session_state.best_combo = max(st. session_state).best_combo, st.session_state.combo)
 st. session_state.해결 += 1
 속도_bonus = int(지금_rem * 2)
 콤보_bonus = (st. session_state. combo - 1) * 20
 = 100 + 속도_bonus + 콤보_bonus 획득
 st.session_state.score += 획득
 st. session_state.best_score = max(st. session_state).best_score, st.session_state.score)
 st. session_state.피드백 = (
 f"✅ 정답! +{gained}점 (기본 100 + 속도 {스피드_bonus} + 콤보 {combo_bonus})"
 )
 그렇지 않으면:
 st.session_state.combo = 0
 st. session_state.틀렸습니다 += 1
 st.session_state.score = max(0, st.session_state.score - 30)
 st. session_state.피드백 = (
 f"❌ 트릭에 걸렸어요! 정답은 **'{q['correct_name']}'** (-30점, 콤보 초기화)"
 )

 st. session_state.역사.append({
 "문제": len(st. session_state).역사,
 "누적점수": st.session_state.score,
 "콤보": st. session_state. combo,
 })
 st.session_state.last_sig = q["sig"]
 st.session_state.q = make_question (prev_sig=st.session_state.last_sig)
 세인트 rerun()

 st.button ("🔄 다시 시작", used_container_width=True):
 init_game ()
 세인트 rerun()
 그렇지 않으면:
 st.success(f" 최고 연속 콤보): **{st.session_state}.best_combo}회** | 세션 최고 기록: **{st.session_state}.best_score}점**)
 st.button ("🚀 새 게임 도전하기", type="primary", user_container_width=True):
 init_game ()
 세인트 rerun()

오른쪽으로:
 세인트 서브헤더 ("📈 점수 & 콤보 기록")
 df = pd.DataFrame(st.session_state).역사).set_index ("문제")
 st.line_chart(df [[ "누적점수"])
 st.line_chart(df [[ "콤보"])
