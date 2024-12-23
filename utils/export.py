from fpdf import FPDF
import streamlit as st

def generate_pdf(mhd_data, board_data, phrases_selected):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Cabeçalho
    pdf.cell(200, 10, txt="Dados Consolidados - Ensino de Ciencia e Xadrez", ln=True, align="C")
    pdf.ln(10)

    # Modelo Hipotético-Dedutivo
    if mhd_data:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Modelo Hipotetico-Dedutivo", ln=True)
        pdf.set_font("Arial", size=12)
        for key, value in mhd_data.items():
            if key and value:
                pdf.multi_cell(0, 10, f"{str(key)}: {str(value)}")
        pdf.ln(5)
    else:
        pdf.cell(200, 10, txt="Sem dados do Modelo Hipotetico-Dedutivo.", ln=True)

    # Tabuleiro
    if board_data:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Configuracao do Tabuleiro", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, str(board_data))  # Garantir que seja string
        pdf.ln(5)
    else:
        pdf.cell(200, 10, txt="Sem configuracao de tabuleiro.", ln=True)

    # Frases Selecionadas
    if phrases_selected:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Frases Selecionadas", ln=True)
        pdf.set_font("Arial", size=12)
        for phrase in phrases_selected:
            if phrase:  # Validar a frase
                pdf.multi_cell(0, 10, str(phrase))  # Garantir que seja string
        pdf.ln(5)
    else:
        pdf.cell(200, 10, txt="Nenhuma frase selecionada.", ln=True)

    return pdf.output(dest="S").encode("latin1")
