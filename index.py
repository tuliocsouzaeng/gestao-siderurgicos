# index.py
import streamlit as st

# ========================================
# 1. INICIALIZAÇÃO
# ========================================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# ========================================
# 2. TELA DE LOGIN
# ========================================
if not st.session_state["logged_in"]:
    st.set_page_config(page_title="Login", layout="centered")
    
    st.title("🔒 Login")

    # Campos de entrada
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if username in st.secrets["credentials"] and st.secrets["credentials"][username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Login realizado com sucesso!")
            st.rerun()  # Recarrega para mostrar o menu
        else:
            st.error("Usuário ou senha incorretos.")

    st.stop()  # Para aqui se não estiver logado

# ========================================
# 3. APÓS LOGIN → LAYOUT WIDE + MENU
# ========================================
st.set_page_config(page_title="NR13 - GOIASA", layout="wide")

# Sidebar com logout
with st.sidebar:
    st.write(f"Usuário: **{st.session_state['username']}**")
    if st.button("Sair"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.rerun()

# ========================================
# 4. NAVEGAÇÃO
# ========================================
pg = st.navigation([
    st.Page("pages/home.py", title="Página Inicial"),
    st.Page("pages/users.py", title="Usuários"),
    st.Page("pages/tanques.py", title="Tanques"),
    st.Page("pages/vasos_de_pressao.py", title="Vasos de Pressão"),
    st.Page("pages/tubulacoes.py", title="Tubulações")
])

pg.run()
