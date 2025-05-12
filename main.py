import streamlit as st

st.title("🧠 넌센스 퀴즈 도전!")

st.header("1. 객관식 퀴즈")
st.write("Q. 소가 도망가면?")

options = ["도망소", "도소", "소도", "소실"]
answer_mc = "도망소"

user_answer_mc = st.radio("정답을 고르세요:", options)

if st.button("객관식 정답 확인"):
    if user_answer_mc == answer_mc:
        st.success("정답입니다! 🎉")
    else:
        st.error(f"오답입니다! 😢 정답은 '{answer_mc}'입니다.")

st.divider()

st.header("2. 주관식 퀴즈")
st.write("Q. 세상에서 가장 지루한 중학교는?")

user_answer_sc = st.text_input("정답을 입력하세요:")

if st.button("주관식 정답 확인"):
    correct_answer_sc = "중언부언중학교"
    if user_answer_sc.strip() == correct_answer_sc:
        st.success("정답입니다! 🎯")
    else:
        st.error(f"아쉽네요! 정답은 '{correct_answer_sc}'입니다.")