import streamlit as st

st.title("Cadastro de Pessoa")

tipo = st.selectbox("Tipo", ["Funcionario", "Cliente"])

nome = st.text_input("Nome")

if tipo == "Funcionario":
    salario = st.number_input("Salário")
    if st.button("Cadastrar Funcionário"):
        st.success(f"Funcionário {nome} cadastrado com salário R$ {salario}")

else:
    profissao = st.text_input("Profissão")
    if st.button("Cadastrar Cliente"):
        st.success(f"Cliente {nome} cadastrado com profissão {profissao}")
