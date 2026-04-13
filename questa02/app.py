import streamlit as st

st.title("Texto de Saída")

texto = st.text_input("Digite o texto")
tamanho = st.slider("Tamanho da letra", 10, 50)
corFonte = st.selectbox("Cor da fonte", ["preto", "branco", "azul", "amarelo", "cinza"])
corFundo = st.selectbox("Cor de fundo", ["preto", "branco", "azul", "amarelo", "cinza"])
tipo = st.selectbox("Tipo", ["label", "edit", "memo"])

if st.button("Exibir"):
    st.write(f"Texto: {texto}")
    st.write(f"Tamanho: {tamanho}")
    st.write(f"Fonte: {corFonte} | Fundo: {corFundo}")
