import streamlit as st 
import random
con_rank=0
point_rank=10
if 'con_rank' not in st.session_state:
        st.session_state.con_rank = con_rank
if 'con_rank' not in st.session_state:
    st.session_state.con_rank = con_rank
if 'money' not in st.session_state:
    st.session_state.money = 0


st.title("パチスロ")
st.header(f"現在の所持金: {st.session_state.money}円")
st.header(f"現在の台の設定: {st.session_state.con_rank}段階")

掛け金=st.number_input("掛け金を入力してください（最低10円）", min_value=10, step=10, value=10)

if st.button("スロットを回す"):
    if st.session_state.money >= 掛け金:
        st.session_state.money -= 掛け金
        slot1 = random.randint(st.session_state.con_rank+1, 7)
        slot2 = random.randint(st.session_state.con_rank+1, 7)
        slot3 = random.randint(st.session_state.con_rank+1, 7)
        st.write(f"スロットの結果: {slot1} - {slot2} - {slot3}")
        if slot1 == slot2 == slot3:
            winnings = 掛け金 * 10
            st.session_state.money += winnings
            st.success(f"おめでとうございます！{winnings}円獲得しました！")
        else:
            st.info("残念、もう一度挑戦してください。")
    else:
        st.warning("所持金が足りません。")