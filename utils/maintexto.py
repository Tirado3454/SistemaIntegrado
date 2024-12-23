import streamlit as st

def adicionar_etapa():
    nova_etapa = {
        "Tópico": st.session_state.topico_selecionado,
        "Descrição": st.session_state.descricao_etapa,
    }
    if nova_etapa in st.session_state.etapas:
        st.warning("Esta etapa já foi adicionada!")
    else:
        st.session_state.etapas.append(nova_etapa)
        st.success("Etapa adicionada com sucesso!")
        st.session_state.descricao_etapa = ""  # Limpar o campo de descrição

    # Atualizar o estado global para integração
    st.session_state["mhd_data"] = st.session_state.etapas

def mhd_function():
    st.title("Modelo Hipotético-Dedutivo no Ensino de Ciências e Xadrez")

    if "etapas" not in st.session_state:
        st.session_state.etapas = []

    # Menu de seleção de tópicos
    topicos = [
        "Observação",
        "Problema",
        "Hipótese",
        "Experimentação",
        "Análise dos Dados",
        "Conclusão"
    ]

    questoes_norteadoras = {
        "Observação": "O que é observado no fenômeno que pode ser explorado?",
        "Problema": "Qual problema pode ser formulado a partir da observação?",
        "Hipótese": "Qual hipótese pode ser levantada para explicar o problema?",
        "Experimentação": "Que experimento pode ser realizado para testar a hipótese?",
        "Análise dos Dados": "O que os dados obtidos dizem sobre a hipótese?",
        "Conclusão": "A hipótese foi confirmada ou refutada? Qual é a conclusão?"
    }

    st.selectbox("Selecione o tópico da etapa:", topicos, key="topico_selecionado")
    st.text_area("Descrição da etapa:", key="descricao_etapa")

    # Exibir questão norteadora correspondente
    topico_atual = st.session_state.topico_selecionado
    if topico_atual in questoes_norteadoras:
        st.info(f"Questão Norteadora: {questoes_norteadoras[topico_atual]}")

    st.button("Adicionar etapa", on_click=adicionar_etapa)

    # Exibir as etapas já adicionadas
    if st.session_state.etapas:
        st.subheader("Etapas do Modelo Hipotético-Dedutivo")
        for idx, etapa in enumerate(st.session_state.etapas):
            st.write(f"**{idx + 1}. {etapa['Tópico']}**")
            st.write(etapa["Descrição"])

    # Atualizar o estado global para integração
    st.session_state["mhd_data"] = st.session_state.etapas
