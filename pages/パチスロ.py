import streamlit as st 

# moneyがまだ初期化されていない場合は初期化
if 'money' not in st.session_state:
    st.session_state.money = 0

st.title("パチスロ")
st.write(f"現在の所持金: {st.session_state.money}円")