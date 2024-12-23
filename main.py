import streamlit as st
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv

# Configuração inicial da página
st.set_page_config(page_title="Ensino de Ciência e Xadrez", layout="wide")

# Inicializar estados globais, se necessário
if "mhd_data" not in st.session_state:
    st.session_state["mhd_data"] = {}
if "board_data" not in st.session_state:
    st.session_state["board_data"] = ""
if "phrases_selected" not in st.session_state:
    st.session_state["phrases_selected"] = []

# Definição do menu de navegação
menu_option = st.sidebar.radio(
    "Escolha uma funcionalidade:",
    ["Modelo Hipotético-Dedutivo", "Editor de Tabuleiro", "Banco de Frases", "Exportar Dados"]
)

# Lógica para cada opção do menu
if menu_option == "Modelo Hipotético-Dedutivo":
    mhd_function()
elif menu_option == "Editor de Tabuleiro":
    board_editor_function()
elif menu_option == "Banco de Frases":
    phrase_bank_function()
elif menu_option == "Exportar Dados":
    st.title("Exportar Dados Consolidados")
    
    # Exibir dados disponíveis
    st.markdown("### Dados do Modelo Hipotético-Dedutivo")
    if st.session_state.get("mhd_data"):
        st.write(st.session_state["mhd_data"])
    else:
        st.warning("Nenhum dado do Modelo Hipotético-Dedutivo disponível.")

    st.markdown("### Configuração do Tabuleiro")
    if st.session_state.get("board_data"):
        st.write(st.session_state["board_data"])
    else:
        st.warning("Nenhuma configuração de tabuleiro disponível.")

    st.markdown("### Frases Selecionadas")
    if st.session_state.get("phrases_selected"):
        st.write(st.session_state["phrases_selected"])
    else:
        st.warning("Nenhuma frase selecionada.")

    # Escolher formato de exportação
    export_format = st.radio("Escolha o formato de exportação:", ["PDF", "CSV"])

    # Botão de exportação
    if st.button("Exportar"):
        if export_format == "PDF":
            pdf_data = generate_pdf(
                st.session_state.get("mhd_data", {}),
                st.session_state.get("board_data", ""),
                st.session_state.get("phrases_selected", [])
            )
            st.download_button(
                label="Baixar PDF",
                data=pdf_data,
                file_name="dados_consolidados.pdf",
                mime="application/pdf"
            )
        elif export_format == "CSV":
            csv_data = generate_csv(
                st.session_state.get("mhd_data", {}),
                st.session_state.get("board_data", ""),
                st.session_state.get("phrases_selected", [])
            )
            st.download_button(
                label="Baixar CSV",
                data=csv_data,
                file_name="dados_consolidados.csv",
                mime="text/csv"
            )
