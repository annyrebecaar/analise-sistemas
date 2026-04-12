import streamlit as st

st.title("Lista de Compras")

nome = st.text_input("Produto")
quantidade = st.number_input("Quantidade", min_value=1)
preco = st.number_input("Preço", min_value=0.0)

if st.button("Calcular Total"):
    total = quantidade * preco
    st.success(f"Total do produto: R$ {total:.2f}")
