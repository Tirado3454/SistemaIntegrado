import streamlit as st

def aplicar_estilo():
    # CSS para personalizar o estilo global
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5;
        }
        .stApp {
            background-image: url("https://via.placeholder.com/1920x1080");
            background-size: cover;
            background-attachment: fixed;
        }
        h1, h2, h3 {
            color: #4CAF50;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
