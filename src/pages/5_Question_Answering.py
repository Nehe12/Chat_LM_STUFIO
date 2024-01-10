import streamlit as st
import requests
from dotenv import load_dotenv
import os

API_ENDPOINT = "https://api-inference.huggingface.co/models/nordGARA/IA-LLAMA"
                # https://api-inference.huggingface.co/endpoints/FlagAlpha/Atom-7B
API_TOKEN = os.getenv("API_TOKEN")

load_dotenv()

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_ENDPOINT, headers=headers, json=payload)
    return response.json()
    # print(response.text)
    

def main():
    st.title("Probando cara abrazada")

    question = st.text_input("Enter your question:", "")

    context = st.text_area("Enter context:", "")

    if st.button("Submit"):
        output = query({
            "inputs": {
                "question": question,
                "context": context
            },
        })

        st.write("Answer:", output.get("answer", "No answer provided"))

if __name__ == "__main__":
    main()
