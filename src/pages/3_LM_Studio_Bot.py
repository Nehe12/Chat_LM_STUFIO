import streamlit as st
from dotenv import load_dotenv
import requests
import json
import os
import openai

openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "NULL"

st.title("💬 Navajo")
st.caption("🚀 No soy responsable si tu trabajo es detectado como plagio")
st.caption("🚀 Es un chat hecho para negros")



if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
if prompt := st.chat_input():
    if not openai.api_base:
        st.info("Please add your OpenAI API base to continue.")
        st.stop()

       
def chat_with_llama(user_input):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    st.chat_message("user").write(user_input, use_container_width=True, unsafe_allow_html=True)
    
    with st.status("Cargando respuesta...",expanded=True)as status:
        try:    
            response = openai.ChatCompletion.create(
                model="gpt-4-0613",
                messages=st.session_state.messages,
                temperature=0.8,
                # max_tokens=500
            )
            msg = response['choices'][0]['message']['content'].strip()
            st.session_state.messages.append({"role": "assistant", "content": msg})          
            st.chat_message("assistant").write(msg, use_container_width=True, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error al obtener respuesta: {str(e)}")
        status.update(label="Respuesta completa!", state="complete")

input_text = st.chat_input("Escribe aquí:")
if input_text:
    chat_with_llama(input_text)
    
    
# if prompt := st.chat_input():
#     if not openai.api_base:
#         st.info("Please add your OpenAI API base to continue.")
#         st.stop()

#     client = OpenAI(api_base=openai.api_base)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)