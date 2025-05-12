import streamlit as st

st.title("😆 웃긴 넌센스 퀴즈")

# 객관식 퀴즈
st.header("1. 객관식 문제")
st.write("Q. 못 팔아도 돈 버는 사람은?")

mc_options = ["노점상", "철물점 주인", "무속인", "판매왕"]
mc_answer = "철물점 주인"

selected = st.radio("정답을 골라보세요!", mc_options)

if st.button("객관식 정답 확인"):
    if selected == mc_answer:
        st.success("정답입니다! 🎉 철물 못 팔아도 돈 벌어요~")
    else:
        st.error(f"오답입니다. 정답은 '{mc_answer}'입니다!")

# 구분선
st.divider()

# 주관식 퀴즈
st.header("2. 주관식 문제")
st.write("Q. 심장의 무게는?")

sc_answer = "두근"
typed = st.text_input("정답을 입력하세요:")

if st.button("주관식 정답 확인"):
    if typed.strip() == sc_answer:
        st.success("정답입니다! 💓 심장은 늘 두근거리죠!")
    else:
        st.error(f"오답입니다. 정답은 '{sc_answer}'입니다.")