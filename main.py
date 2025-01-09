import streamlit as st
from design import aplicar_estilo  # Estilos globais
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv

# Configuração inicial da página
st.set_page_config(page_title="Ensino de Ciência e Xadrez", layout="wide")

# Aplicar estilo global
aplicar_estilo()

# Título principal
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50;">Ensino de Ciência e Xadrez</h1>
    <p style="text-align: center; color: #555;">Explore conteúdos, ferramentas interativas e recursos didáticos.</p>
    """,
    unsafe_allow_html=True
)

# Menu principal
menu_type = st.sidebar.radio(
    "📂 **Navegação**",
    ["📖 Textos", "⚙️ Funcionalidades", "🗂 Planejamento"]
)

if menu_type == "📖 Textos":
    text_option = st.sidebar.radio(
        "Escolha um conteúdo:",
        ["Modelo Hipotético-Dedutivo"]
    )
    if text_option == "Modelo Hipotético-Dedutivo":
        mhd_function()

elif menu_type == "⚙️ Funcionalidades":
    func_option = st.sidebar.radio(
        "Escolha uma funcionalidade:",
        ["Editor de Tabuleiro", "Banco de Frases", "Exportar Dados"]
    )
    if func_option == "Editor de Tabuleiro":
        board_editor_function()
    elif func_option == "Banco de Frases":
        phrase_bank_function()
    elif func_option == "Exportar Dados":
        st.title("Exportar Dados Consolidados")
        export_format = st.radio("Formato:", ["PDF", "CSV"])
        if st.button("Exportar"):
            if export_format == "PDF":
                pdf_data = generate_pdf()
                st.download_button("Baixar PDF", data=pdf_data, file_name="dados.pdf", mime="application/pdf")
            elif export_format == "CSV":
                csv_data = generate_csv()
                st.download_button("Baixar CSV", data=csv_data, file_name="dados.csv", mime="text/csv")

elif menu_type == "🗂 Planejamento":
    st.title("Planejamento de Aula")
    st.markdown("Aqui você pode criar, visualizar e exportar planejamentos de aula.")
