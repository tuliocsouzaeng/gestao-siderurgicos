import streamlit as st
import pandas as pd


pg = st.navigation([
    st.Page("pages/home.py", title="Página Inicial"),
    st.Page("pages/users.py", title="Usuários"),
    st.Page("pages/tanques.py", title="Tanques"),
    st.Page("pages/vasos_de_pressao.py", title="Vasos de Pressão"),
    st.Page("pages/tubulacoes.py", title="Tubulações")
])

pg.run()