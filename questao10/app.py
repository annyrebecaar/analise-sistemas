import streamlit as st

st.title("Agendamento de Reunião")

funcionario = st.text_input("Funcionário")
sala = st.text_input("Sala")
data = st.date_input("Data")
horario = st.time_input("Horário")

if st.button("Agendar"):
    st.success(f"Reunião marcada por {funcionario} na sala {sala}")
