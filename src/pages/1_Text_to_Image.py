import streamlit as st
import json
import requests
from PIL import Image
import io
import re
from time import time


API_TOKEN = ""  
headers = {
    # "Authorization": f"Bearer {API_TOKEN}",
    "X-Wait-For-Model": "true",
    "X-Use-Cache": "false"
}
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return Image.open(io.BytesIO(response.content))


def slugify(text):
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


def main():
    st.title("Stable-Diffusion Inferencia de Cara Abrazada")
    
    prompt = st.text_input("Enter a prompt:")
    
    if st.button("Generate Image"):
        with st.status("Generando imagen...",expanded=True)as status:
            try:    
                image = query({
                    "inputs": prompt,
                    "temperatura":0.7
                    })
                
                st.image(image, caption="Generated Image", use_column_width=True)
                
                image.save(f"{slugify(prompt)}-{time():.0f}.png")
                st.success("Image generated and saved successfully!")
            except Exception as e:
                st.error(f"Error al obtener respuesta: {str(e)}")
        status.update(label="Imagen completa!", state="complete")

if __name__ == "__main__":
    main()



# import streamlit as st
# from dotenv import load_dotenv
# import requests
# import json
# import os
# import openai

# openai.api_key= os.getenv("OPENAI_API_KEY")
# key = os.getenv("STABLE_DIFUSION_API_KEY")
# # url = "https://stablediffusionapi.com/api/v3/img2img"
# url = "https://stablediffusionapi.com/api/v3/text2img"

# load_dotenv()

# st.title("Generador de imagenes con Stable Difusion")

# with st.form("images-form"):
#     text = st.text_input("Texto para generar imagenes")
#     text_neg = st.text_input("Prompt negativo")
#     num_img = st.number_input("Numero de imagenes a generar", min_value=1, max_value=5, value=1)
#     # image_size = st.selectbox("Tamaño de la imagen",["256x256","512x512","1024x1024"],index=0)
#     width = st.selectbox("Ancho de la imagen", ["256", "512", "1024"], index=1)
#     height = st.selectbox("Alto de la imagen", ["256", "512", "1024"], index=1)
#     submit_button = st.form_submit_button(label="Generar Imagenes")


# if submit_button:
#     st.write("Generando imagenes...")
    
#     payload = json.dumps({
#         "key": key,
#         "prompt": text,
#         "negative_prompt": text_neg,
#         "width": width,
#         "height": height,
#         "samples": "1",
#         "num_inference_steps": "20",
#         "seed": None,
#         "guidance_scale": 7.5,
#         "safety_checker": "yes",
#         "multi_lingual": "no",
#         "panorama": "no",
#         "self_attention": "no",
#         "upscale": "no",
#         "embeddings_model": None,
#         "webhook": None,
#         "track_id": None
#         })

#     headers = {
#     'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)
    
#     print(response.text)
#     if response.status_code == 200:
#         try:
#             data = response.json()
#             output_images = data.get("output", [])
#             if not output_images:
#                 st.warning("No output images found in the response.")
#             else:
#                 for i, image_url in enumerate(output_images):
#                     st.image(image_url, caption=f"Image {i+1}", use_column_width=True)
#         except json.JSONDecodeError:
#             st.error("Error decoding JSON response from the API.")
#     else:
#         st.error(f"Error in the request: {response.status_code} - {response.text}")
        
# data = response.json()
    # print(response.json())
       
    # for i in range(response.data):
    #     url = response.data[i].url
    #     st.image(url,caption==f"Imagen{i+1}",use_column_width=True)
    # print(response.text)        
        
        # DALL-E
    
# if submit_button:
#     st.write("Generando imagenes...")
#     response = openai.Image.create(
#         prompt = text,
#         n=num_img,
#         size= image_size
#     )
    # print(response)