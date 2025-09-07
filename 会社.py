import streamlit as st

money=0
worked=0
rank=0
if 'money' not in st.session_state:
    st.session_state.money = money
elif 'worked' not in st.session_state:
    st.session_state.worked = worked
elif 'rank' not in st.session_state:
    st.session_state.rank = rank
st.title("会社")
st.write(f"現在のランク: {st.session_state.rank}")
st.write(f"現在の所持金: {st.session_state.money}円")
if st.button("お金を稼ぐ"):
    st.session_state.money += rank+10
    st.session_state.worked += 1

if st.session_state.worked >= 15:
    st.session_state.rank += 1
    st.session_state.worked = 0
    st.balloons()
    st.success("ランクアップしました！")

