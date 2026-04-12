import streamlit as st

st.title("Cadastro de CDs")

artista = st.text_input("Nome do Artista")
cd = st.text_input("Título do CD")
ano = st.number_input("Ano de Lançamento", min_value=1900)

if st.button("Cadastrar"):
    st.success(f"CD '{cd}' do artista {artista} cadastrado!")
