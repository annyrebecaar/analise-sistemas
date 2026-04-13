import streamlit as st

st.title("Conta de Luz")

data = st.date_input("Data da leitura")
leitura = st.number_input("Número da leitura", min_value=0)
kw = st.number_input("KW gasto", min_value=0)
valor = st.number_input("Valor a pagar", min_value=0.0)
pagamento = st.date_input("Data de pagamento")

if st.button("Registrar"):
    media = kw / 30
    st.success(f"Média de consumo: {media:.2f} KW/dia")
