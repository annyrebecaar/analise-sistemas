import streamlit as st

st.title("Controle de Remédios")

nome = st.text_input("Nome da pessoa")
remedio = st.text_input("Nome do remédio")
dias = st.number_input("Quantidade de dias", min_value=1)
vezes = st.number_input("Vezes ao dia", min_value=1)
dosagem = st.text_input("Dosagem")

if st.button("Gerar horários"):
    st.success(f"{nome} deve tomar {remedio} {vezes}x ao dia por {dias} dias")
