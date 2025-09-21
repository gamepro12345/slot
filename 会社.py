import streamlit as st

money=0
worked=0
rank=0
if 'money' not in st.session_state:
    st.session_state.money = money
if 'worked' not in st.session_state:
    st.session_state.worked = worked
if 'rank' not in st.session_state:
    st.session_state.rank = rank
st.title("会社")
st.header(f"現在のランク: {st.session_state.rank}")

# 画像を表示（例: rank.png）


st.header(f"現在の所持金: {st.session_state.money}円")
if st.button("お金を稼ぐ"):
    st.session_state.money += st.session_state.rank+10000000000000
    st.session_state.worked += 1

if st.session_state.worked >= 15:
    st.session_state.rank += 1
    st.session_state.worked = 0
    st.success("ランクアップしました！")
st.image("ビル.png")