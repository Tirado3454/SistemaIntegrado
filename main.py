import streamlit as st
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv

st.set_page_config(page_title="Ensino de Ciência e Xadrez", layout="wide")

# Menu de navegação
menu_option = st.sidebar.radio(
    "Escolha uma funcionalidade:",
    ["Modelo Hipotético-Dedutivo", "Editor de Tabuleiro", "Banco de Frases", "Exportar Dados"]
)

# Dados globais
if "mhd_data" not in st.session_state:
    st.session_state.mhd_data = {}
if "board_data" not in st.session_state:
    st.session_state.board_data = ""
if "phrases_selected" not in st.session_state:
    st.session_state.phrases_selected = []

# Navegação entre módulos
if menu_option == "Modelo Hipotético-Dedutivo":
    mhd_function()
elif menu_option == "Editor de Tabuleiro":
    board_editor_function()
elif menu_option == "Banco de Frases":
    phrase_bank_function()
elif menu_option == "Exportar Dados":
    st.title("Exportar Dados Consolidado")
    st.markdown("### Dados do Modelo Hipotético-Dedutivo")
    st.write(st.session_state.mhd_data)
    st.markdown("### Configuração do Tabuleiro")
    st.write(st.session_state.board_data)
    st.markdown("### Frases Selecionadas")
    st.write(st.session_state.phrases_selected)

    export_format = st.radio("Escolha o formato de exportação:", ["PDF", "CSV"])

    if st.button("Exportar"):
        if export_format == "PDF":
            generate_pdf(st.session_state.mhd_data, st.session_state.board_data, st.session_state.phrases_selected)
        elif export_format == "CSV":
            generate_csv(st.session_state.mhd_data, st.session_state.board_data, st.session_state.phrases_selected)
