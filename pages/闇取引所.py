import streamlit as st
# moneyがまだ初期化されていない場合は初期化
if 'money' not in st.session_state:
    st.session_state.money = 0
if 'con_rank' not in st.session_state:
    st.session_state.con_rank = 0
if 'point_rank' not in st.session_state:
    st.session_state.point_rank = 10

st.title("闇取引所")
st.header(f"現在の所持金: {st.session_state.money}円")
st.header(f"現在の台の設定: {st.session_state.con_rank}段階")
st.header(f"現在の倍率: {st.session_state.con_rank}倍")
if st.session_state.con_rank < 6:
    if st.button("台の設定を上げる（5000円）"):
        if st.session_state.money >= 5000:
            st.session_state.money -= 5000
            st.session_state.con_rank += 1
            st.success("台の設定を上げました！")
        else:
            st.warning("所持金が足りません。")
else:
    st.info("これ以上台の設定を上げることはできません。")
if st.session_state.point_rank < 100:
    if st.button("倍率を上げる（1000円）"):
        if st.session_state.money >= 1000:
            st.session_state.money -= 1000
            st.session_state.point_rank += 1
            st.success("倍率を上げました！")
        else:
            st.warning("所持金が足りません。")
else:
    st.info("これ以上倍率を上げることはできません。")
