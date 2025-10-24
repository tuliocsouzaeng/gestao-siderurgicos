import streamlit as st
import pandas as pd

st.title("🔒 Login")

# Campos de entrada
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

# Validação
if st.button("Entrar"):
    if username in st.secrets["credentials"] and st.secrets["credentials"][username] == password:
        st.session_state["logged_in"] = True
        st.success("Login realizado com sucesso!")
    else:
        st.error("Usuário ou senha incorretos.")

# Mostra conteúdo só se estiver logado
if st.session_state.get("logged_in"):
    st.write("✅ Bem-vindo, ", username)
    # aqui entra o resto do app (dataframes, gráficos, etc.)
    pg = st.navigation([
        st.Page("pages/home.py", title="Página Inicial"),
        st.Page("pages/users.py", title="Usuários"),
        st.Page("pages/tanques.py", title="Tanques"),
        st.Page("pages/vasos_de_pressao.py", title="Vasos de Pressão"),
        st.Page("pages/tubulacoes.py", title="Tubulações")
    ])
    
    pg.run()
