import streamlit as st

st.title("Gastos Diários")

tipo = st.text_input("Tipo de gasto")
data = st.date_input("Data")
valor = st.number_input("Valor", min_value=0.0)

pagamento = st.selectbox("Forma de pagamento", [
    "Dinheiro", "Cartão Crédito", "Cartão Débito", "Ticket Alimentação", "Refeição"
])

if st.button("Adicionar gasto"):
    st.success(f"Gasto registrado: {tipo} - R$ {valor}")
