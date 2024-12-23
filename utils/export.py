from fpdf import FPDF
import streamlit as st

def generate_pdf(mhd_data, board_data, phrases_selected):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Dados Consolidados - Ensino de Ciência e Xadrez", ln=True, align="C")
    pdf.ln(10)

    # Dados do MHD
    if mhd_data:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Modelo Hipotético-Dedutivo", ln=True)
        pdf.set_font("Arial", size=12)
        for key, value in mhd_data.items():
            if key and value:  # Verificar se os dados não estão vazios
                pdf.multi_cell(0, 10, f"{key}: {value}")
        pdf.ln(5)
    else:
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Sem dados do Modelo Hipotético-Dedutivo.", ln=True)

    pdf.ln(5)  # Separador
    # Dados do Tabuleiro
    if board_data:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Configuração do Tabuleiro", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, board_data)
        pdf.ln(5)
    else:
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Sem configuração de tabuleiro.", ln=True)

    pdf.ln(5)  # Separador
    # Frases Selecionadas
    if phrases_selected:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Frases Selecionadas", ln=True)
        pdf.set_font("Arial", size=12)
        for phrase in phrases_selected:
            if phrase:  # Verificar se a frase não está vazia
                pdf.multi_cell(0, 10, phrase)
        pdf.ln(5)
    else:
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Nenhuma frase selecionada.", ln=True)

    pdf_output = pdf.output(dest="S").encode("latin1")
    st.download_button(
        label="Baixar PDF",
        data=pdf_output,
        file_name="dados_consolidados.pdf",
        mime="application/pdf",
    )
