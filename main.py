if menu_option == "Modelo Hipotético-Dedutivo":
    mhd_function()
elif menu_option == "Editor de Tabuleiro":
    board_editor_function()
elif menu_option == "Banco de Frases":
    phrase_bank_function()
elif menu_option == "Exportar Dados":
    st.title("Exportar Dados Consolidado")
    st.markdown("### Dados do Modelo Hipotético-Dedutivo")
    if st.session_state.mhd_data:
        st.write(st.session_state.mhd_data)
    else:
        st.warning("Nenhum dado do Modelo Hipotético-Dedutivo disponível.")

    st.markdown("### Configuração do Tabuleiro")
    if st.session_state.board_data:
        st.write(st.session_state.board_data)
    else:
        st.warning("Nenhuma configuração de tabuleiro disponível.")

    st.markdown("### Frases Selecionadas")
    if st.session_state.phrases_selected:
        st.write(st.session_state.phrases_selected)
    else:
        st.warning("Nenhuma frase selecionada.")

    export_format = st.radio("Escolha o formato de exportação:", ["PDF", "CSV"])

    if st.button("Exportar"):
        if export_format == "PDF":
            if st.session_state.mhd_data or st.session_state.board_data or st.session_state.phrases_selected:
                generate_pdf(st.session_state.mhd_data, st.session_state.board_data, st.session_state.phrases_selected)
            else:
                st.warning("Não há dados disponíveis para exportar.")
        elif export_format == "CSV":
            if st.session_state.mhd_data or st.session_state.board_data or st.session_state.phrases_selected:
                generate_csv(st.session_state.mhd_data, st.session_state.board_data, st.session_state.phrases_selected)
            else:
                st.warning("Não há dados disponíveis para exportar.")
