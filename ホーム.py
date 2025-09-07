import streamlit as st

money=0

if 'money' not in st.session_state:
    st.session_state.money = money

st.title("ホーム")
st.write(f"現在の所持金: {st.session_state.money}円")
if st.button("お金を稼ぐ"):
    st.session_state.money += 10

