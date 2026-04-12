import streamlit as st

st.title("Coleção de CDs")

cd = st.text_input("Nome do CD")
artistas = st.text_input("Artistas (separados por vírgula)")
musica = st.text_input("Nome da Música")
duracao = st.text_input("Duração")

if st.button("Adicionar"):
    st.success(f"Música '{musica}' adicionada ao CD '{cd}'")
