import streamlit as st

st.title("Boneco em Movimento")

nome = st.text_input("Nome do boneco")
x = st.number_input("Posição X", min_value=0)
y = st.number_input("Posição Y", min_value=0)

direcao = st.selectbox("Direção", ["Cima", "Baixo", "Direita", "Esquerda"])

if st.button("Mover"):
    st.success(f"{nome} movido para {direcao} na posição ({x}, {y})")
