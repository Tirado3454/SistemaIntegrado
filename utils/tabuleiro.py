import streamlit as st
import chess
import chess.svg

def board_editor_function():
    # Inicialização do tabuleiro no estado global
    if "current_board" not in st.session_state:
        st.session_state.current_board = chess.Board()
    if "board_data" not in st.session_state:
        st.session_state.board_data = st.session_state.current_board.fen()

    # Função para renderizar o tabuleiro com estilo customizado
    def render_tabuleiro_customizado(board):
        return chess.svg.board(
            board=board, 
            size=320,  # Tamanho do tabuleiro
            style=""" 
                .square.light { fill: #ffffff; }  /* Casas claras em branco */
                .square.dark { fill: #8FBC8F; }  /* Casas escuras em verde */
            """
        )

    # Configuração do tabuleiro com FEN
    st.subheader("Configuração do Tabuleiro")
    fen_input = st.text_input(
        "Insira a notação FEN para configurar o tabuleiro:", 
        value=st.session_state.current_board.fen(),
        help="Insira uma configuração FEN válida para alterar o tabuleiro."
    )

    if st.button("Atualizar Tabuleiro com FEN"):
        try:
            st.session_state.current_board.set_fen(fen_input)
            st.session_state.board_data = st.session_state.current_board.fen()
            st.success("Tabuleiro atualizado com sucesso!")
        except ValueError:
            st.error("Notação FEN inválida. Por favor, insira uma notação correta.")

    # Visualizar tabuleiro configurado
    st.subheader("Tabuleiro Atual")
    st.image(render_tabuleiro_customizado(st.session_state.current_board), use_container_width=True)

    # Mostrar a FEN atual
    st.subheader("Notação FEN Atual")
    st.code(st.session_state.board_data, language="text")
