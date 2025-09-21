import streamlit as st

if 'money' not in st.session_state:
    st.session_state.money = 0
if 'con_rank' not in st.session_state:
    st.session_state.con_rank = 0
if 'point_rank' not in st.session_state:
    st.session_state.point_rank = 10
if 'limit_enabled' not in st.session_state:
    st.session_state.limit_enabled = True  # 制限ONが初期値

st.title("闇取引所")
st.header(f"現在の所持金: {st.session_state.money}円")
st.header(f"現在の台の設定: {st.session_state.con_rank}段階")
st.header(f"現在の倍率: {st.session_state.point_rank}倍")

# 制限のON/OFF切り替えボタン
if st.button(f"制限 {'OFF' if st.session_state.limit_enabled else 'ON'}に切り替え"):
    st.session_state.limit_enabled = not st.session_state.limit_enabled

if st.session_state.limit_enabled:
    # 制限あり
    if st.session_state.con_rank < 4:
        if st.button("台の設定を上げる（5000円）"):
            if st.session_state.money >= 5000:
                st.session_state.money -= 5000
                st.session_state.con_rank += 1
                st.success("台の設定を上げました！")
            else:
                st.warning("所持金が足りません。")
    else:
        st.info("これ以上台の設定を上げることはできません。")
    if st.session_state.point_rank < 20:
        if st.button("倍率を上げる（1000円）"):
            if st.session_state.money >= 1000:
                st.session_state.money -= 1000
                st.session_state.point_rank += 1
                st.success("倍率を上げました！")
            else:
                st.warning("所持金が足りません。")
    else:
        st.info("これ以上倍率を上げることはできません。")
else:
    # 制限なし
    if st.button("台の設定を上げる（5000円）"):
        if st.session_state.money >= 5000:
            st.session_state.money -= 5000
            st.session_state.con_rank += 1
            st.success("台の設定を上げました！（制限なし）")
        else:
            st.warning("所持金が足りません。")
    if st.button("倍率を上げる（1000円）"):
        if st.session_state.money >= 1000:
            st.session_state.money -= 1000
            st.session_state.point_rank += 1
            st.success("倍率を上げました！（制限なし）")
        else:
            st.warning("所持金が足りません。")
