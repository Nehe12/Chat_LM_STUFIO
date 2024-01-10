import streamlit as st
from dotenv import load_dotenv
import requests
import json
import os
import openai

# def main():
st.title("🚀 Welcome to Your Life")
st.write("¡Explora y experimenta las maravillas de tu vida con Chat BLACK!")

st.header("Chat BLACK")
st.write("Participe en conversaciones significativas y descubra más sobre usted mismo.")

# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Choose a Page", ["Welcome", "Chat BLACK"])

# if page == "Welcome":
#     show_welcome_page()
# elif page == "Chat BLACK":
#     show_chat_black_page()

# def show_welcome_page():
st.header("Welcome to Chat BLACK")
image_path = "images/universidad_1106_g_63951.png"
st.image("https://sic.cultura.gob.mx/imagenes_cache/universidad_1106_g_63951.png", caption="", use_column_width=True)
st.write("Chat BLACK es una plataforma diseñada para brindarte una experiencia única e interactiva. ¡Sumérgete en conversaciones, explora tus pensamientos y disfruta el viaje!")

st.subheader("Getting Started")
st.write("Para comenzar, navegue hasta la página 'Chat BLACK' usando la barra lateral. Participe en conversaciones, haga preguntas y deje que Chat BLACK sea su compañero en este viaje.")

# def show_chat_black_page():
st.header("Chat BLACK")
st.write("Engage in conversations with Chat BLACK. Ask questions, share your thoughts, and explore the depths of your mind.")
    
    
# if __name__ == "__main__":
#     main()