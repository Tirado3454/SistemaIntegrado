from fpdf import FPDF
import streamlit as st

def generate_pdf(mhd_data, board_data, phrases_selected):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Cabeçalho principal
    pdf.cell(200, 10, txt="Relatório do Modelo Hipotético-Dedutivo", ln=True, align="C")
    pdf.ln(10)

    # Modelo Hipotético-Dedutivo
    if mhd_data:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Modelo Hipotético-Dedutivo", ln=True)
        pdf.set_font("Arial", size=12)
        for idx, etapa in enumerate(mhd_data):
            pdf.cell(200, 10, txt=f"Etapa {idx + 1}: {etapa['Tópico']}", ln=True)
            pdf.multi_cell(0, 10, etapa["Descrição"])
            pdf.ln(5)
    else:
        pdf.cell(200, 10, txt="Nenhuma etapa do Modelo Hipotético-Dedutivo foi encontrada.", ln=True)

    pdf.ln(5)

    # Configuração do Tabuleiro
    if board_data:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Configuração do Tabuleiro", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, str(board_data))
        pdf.ln(5)
    else:
        pdf.cell(200, 10, txt="Sem configuração do tabuleiro.", ln=True)

    pdf.ln(5)

    # Frases Selecionadas
    if phrases_selected:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Frases Selecionadas", ln=True)
        pdf.set_font("Arial", size=12)
        for phrase in phrases_selected:
            pdf.multi_cell(0, 10, str(phrase))
            pdf.ln(5)
    else:
        pdf.cell(200, 10, txt="Nenhuma frase selecionada.", ln=True)

    return pdf.output(dest="S").encode("latin1")

# Função para integrar ao botão de download
def setup_download_buttons(mhd_data, board_data, phrases_selected):
    pdf_data = generate_pdf(mhd_data, board_data, phrases_selected)
    st.download_button(
        label="Baixar Relatório em PDF",
        data=pdf_data,
        file_name="relatorio_mhd.pdf",
        mime="application/pdf"
    )
