import streamlit as st
import requests
from dotenv import load_dotenv
import os

API_ENDPOINT = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
                # https://api-inference.huggingface.co/endpoints/FlagAlpha/Atom-7B
API_TOKEN = os.getenv("API_TOKEN_CHAT")

load_dotenv()

headers = {"Authorization": f"Bearer {API_TOKEN}"}

st.title("💬 Dialog Chat")
st.caption("🚀 Preguntame Carnal")
st.caption("🚀 Es un chat hecho para negros")

# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

def query(payload):
    response = requests.post(API_ENDPOINT, headers=headers, json=payload)
    return response.json()
    # print(response)

def chat_gpt2(prompt):
    # st.session_state.messages.append({"role": "user", "content": prompt})
    
    st.chat_message("user").write(prompt, use_container_width=True, unsafe_allow_html=True)
    
    with st.spinner("Cargando respuesta..."):
        try:
            output = query({
                "inputs": {
                    "past_user_inputs": ["Which movie is the best ?"],
                    "generated_responses": ["It is Die Hard for sure."],
                    "text": prompt
                    },
                "temperature":10,
                "tokens":500
            })
            st.write(output)
            # msg = output[0].get('generated_text', '').strip()
            msg = output['generated_text'].strip()    
            # st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg, use_container_width=True, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error al obtener respuesta: {str(e)}")

prompt = st.chat_input("Escribe aquí:")
if prompt:
    chat_gpt2(prompt)
