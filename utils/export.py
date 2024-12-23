from fpdf import FPDF
import pandas as pd
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

def generate_csv(mhd_data, board_data, phrases_selected):
    rows = []

    # Modelo Hipotético-Dedutivo
    if mhd_data:
        for key, value in mhd_data.items():
            rows.append({"Categoria": "Modelo Hipotético-Dedutivo", "Descrição": f"{key}: {value}"})

    # Tabuleiro
    if board_data:
        rows.append({"Categoria": "Configuração do Tabuleiro", "Descrição": board_data})

    # Frases Selecionadas
    if phrases_selected:
        for phrase in phrases_selected:
            rows.append({"Categoria": "Frases Selecionadas", "Descrição": phrase})

    # Gerar CSV
    df = pd.DataFrame(rows)
    return df.to_csv(index=False).encode("utf-8")
