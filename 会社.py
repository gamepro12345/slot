import streamlit as st

money=0
worked=0
if 'money' not in st.session_state:
    st.session_state.money = money
elif 'worked' not in st.session_state:
    st.session_state.worked = worked
st.title("ホーム")
st.write(f"現在の所持金: {st.session_state.money}円")
if st.button("お金を稼ぐ"):
    st.session_state.money += 10
    st.session_state.worked += 1

