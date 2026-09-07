import streamlit as st
from app import app

st.set_page_config(
    page_title="AI Decision Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render Gradio inside Streamlit cleanly
app.launch(share=False, embed_page=True, inline=True)