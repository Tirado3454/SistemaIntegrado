from fpdf import FPDF
import pandas as pd
import streamlit as st
from datetime import datetime

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
            pdf.multi_cell(0, 10, phrase)
        pdf.ln(5)
    else:
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Nenhuma frase selecionada.", ln=True)

    pdf_output = pdf.output(dest="S").encode("latin1")
    filename = f"dados_consolidados_{datetime.now().strftime('%Y%m%d')}.pdf"
    st.download_button(
        label="Baixar PDF",
        data=pdf_output,
        file_name=filename,
        mime="application/pdf",
    )

def generate_csv(mhd_data, board_data, phrases_selected):
    if not mhd_data and not board_data and not phrases_selected:
        st.warning("Nenhum dado disponível para exportação.")
        return

    rows = []

    # Adicionar dados do MHD
    if mhd_data:
        for key, value in mhd_data.items():
            rows.append({"Categoria": "Modelo Hipotético-Dedutivo", "Descrição": f"{key}: {value}"})

    # Adicionar dados do Tabuleiro
    if board_data:
        rows.append({"Categoria": "Configuração do Tabuleiro", "Descrição": board_data})

    # Adicionar frases selecionadas
    if phrases_selected:
        for phrase in phrases_selected:
            rows.append({"Categoria": "Frases Selecionadas", "Descrição": phrase})

    df = pd.DataFrame(rows)
    csv_data = df.to_csv(index=False).encode("utf-8")
    filename = f"dados_consolidados_{datetime.now().strftime('%Y%m%d')}.csv"
    st.download_button(
        label="Baixar CSV",
        data=csv_data,
        file_name=filename,
        mime="text/csv",
    )
