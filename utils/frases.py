import streamlit as st
import pandas as pd
from fpdf import FPDF

def phrase_bank_function():
    # Banco de frases completo
    frases_por_titulo = {
        "Método Científico e a Evolução da Ciência": [
            "O método científico é uma abordagem sistemática para entender o mundo natural.",
            "A ciência evolui com base em observações, hipóteses, experimentos e análises.",
            # Insira todas as 30 frases para este tema
        ],
        "Sem Método Científico e Fatores Insólitos": [
            "Sem o método científico, nossas explicações para fenômenos naturais seriam baseadas em mitos e superstições.",
            "A humanidade viveria à mercê de crenças infundadas e dogmas inquestionáveis.",
            # Insira todas as 30 frases para este tema
        ],
        "Como o Cientista Deve Proceder": [
            "O cientista deve basear-se em dados e evidências, evitando preconceitos.",
            "A neutralidade e a objetividade são essenciais para validar descobertas científicas.",
            # Insira todas as 30 frases para este tema
        ],
        "Pensadores que Mudaram os Métodos Científicos": [
            "Galileu Galilei demonstrou a importância da observação e do experimento.",
            "Francis Bacon enfatizou o empirismo como base do conhecimento.",
            # Insira todas as 30 frases para este tema
        ],
    }

    # Inicializar estado
    if "phrases_selected" not in st.session_state:
        st.session_state["phrases_selected"] = []

    # Título do programa
    st.title("Banco de Frases para Aulas")
    st.markdown("### Selecione frases organizadas por categorias para sua aula.")

    # Armazenar seleções
    selecoes = {}

    # Exibir categorias e frases
    for titulo, frases in frases_por_titulo.items():
        with st.expander(f"Categoria: {titulo}"):
            selecoes[titulo] = []
            for frase in frases:
                if st.checkbox(frase, key=f"{titulo}_{frase}"):
                    selecoes[titulo].append(frase)

    # Botão para organizar e exportar frases
    st.markdown("### Revisar e Exportar Frases Selecionadas")
    if st.button("Organizar e Exportar"):
        frases_selecionadas = [
            {"Categoria": titulo, "Frase": frase}
            for titulo, frases_categoria in selecoes.items()
            for frase in frases_categoria
        ]
        if frases_selecionadas:
            # Salvar no estado global
            st.session_state["phrases_selected"] = frases_selecionadas

            # Exibir as frases selecionadas
            st.markdown("### Frases Selecionadas:")
            for item in frases_selecionadas:
                st.markdown(f"- **{item['Categoria']}:** {item['Frase']}")

            # Exportar para CSV
            df = pd.DataFrame(frases_selecionadas)
            csv_data = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Baixar como CSV",
                data=csv_data,
                file_name="frases_selecionadas.csv",
                mime="text/csv",
            )

            # Exportar para PDF
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Frases Selecionadas para Aula", ln=True, align="C")
            pdf.ln(10)
            for item in frases_selecionadas:
                pdf.set_font("Arial", style="B", size=12)
                pdf.cell(200, 10, txt=f"Categoria: {item['Categoria']}", ln=True)
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, item["Frase"])
                pdf.ln(5)
            pdf_output = pdf.output(dest="S").encode("latin1")
            st.download_button(
                label="Baixar como PDF",
                data=pdf_output,
                file_name="frases_selecionadas.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("Nenhuma frase foi selecionada.")
