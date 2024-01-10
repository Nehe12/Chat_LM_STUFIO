import streamlit as st
from dotenv import load_dotenv
import requests
import json
import os 

url = "https://stablediffusionapi.com/api/v3/img2img"
key = os.getenv("STABLE_DIFUSION_API_KEY")
load_dotenv()

st.title("IMAGE TO IMAGE")

with st.form("fom-images"):
    url= st.file_uploader("Cargar imagen")
    text2 = st.text_input("Texto para generar imagenes")
    submit_button = st.form_submit_button(label="Cambiar Imagenes")
    
if submit_button:
    st.write("Transforamdo imagen")
    payload = json.dumps({
    "key": key,
    "prompt": "a cat sitting on a bench",
    "negative_prompt": None,
    "init_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "safety_checker": "no",
    "enhance_prompt": "yes",
    "guidance_scale": 7.5,
    "strength": 0.7,
    "base64": "no",
    "seed": None,
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)