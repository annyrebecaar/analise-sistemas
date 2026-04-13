import streamlit as st

st.title("Comanda Eletrônica")

numero = st.number_input("Número da comanda", min_value=1)

produto = st.text_input("Produto")
quantidade = st.number_input("Quantidade", min_value=1)
preco = st.number_input("Valor unitário", min_value=0.0)

if st.button("Calcular total"):
    total = quantidade * preco
    st.success(f"Total da comanda {numero}: R$ {total:.2f}")
