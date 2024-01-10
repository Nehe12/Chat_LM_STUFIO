import streamlit as st
import base64
import hashlib
from time import sleep
from PIL import Image
import httpx
import io
import os
from dotenv import load_dotenv

API_KEY = os.getenv("REMINI_API_KEY")
BASE_URL = "https://developer.remini.ai/api"

load_dotenv()

def enhance_image(file_content):
    image_md5, content = _get_image_md5_content(file_content)
    
    with httpx.Client(
        base_url=BASE_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
    ) as client:
        response = client.post(
            "/tasks",
            json={
                "tools": [
                    {"type": "face_enhance", "mode": "beautify"},
                    {"type": "background_enhance", "mode": "base"}
                ],
                "image_md5": image_md5,
                "image_content_type": "image/jpeg",
                "output_content_type": "image/jpeg"
            }
        )
        
        try:
            response.raise_for_status()
            assert response.status_code == 200
        except httpx.HTTPStatusError as e:
            st.error(f"Error HTTP: {e}")
            st.error(f"Contenido de la respuesta: {response.text}")
            st.error(f"Código de estado: {response.status_code}")
            return
        except AssertionError:
            st.error("Error: La respuesta no tiene un código de estado 200")
            st.error(f"Contenido de la respuesta: {response.text}")
            st.error(f"Código de estado: {response.status_code}")
            return

        body = response.json()
        task_id = body["task_id"]

        response = client.put(
            body["upload_url"], headers=body["upload_headers"],
            content=content, timeout=60
        )
        assert response.status_code == 200

        response = client.post(f"/tasks/{task_id}/process")
        assert response.status_code == 202

        for i in range(50):
            response = client.get(f"/tasks/{task_id}")
            assert response.status_code == 200

            if response.json()["status"] == "completed":
                break
            else:
                sleep(2)

        return response.json()["result"]["output_url"]

def _get_image_md5_content(file_content):
    content = file_content.read()
    image_md5 = base64.b64encode(hashlib.md5(content).digest()).decode("utf-8")
    return image_md5, content

st.title("Mejorar imagen con Remini")
st.caption("🚀 Este filtro es excluivamene para blacks")
st.caption("🚀 No te ofendas si no funciona contigo")

uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Imagen cargada", use_column_width=True)
    
    if st.button("Mejorar imagen"):
        st.text("Mejorando imagen. Por favor, espera...")
        output_url = enhance_image(uploaded_file)
        
        enhanced_image_content = httpx.get(output_url).content
        enhanced_image = Image.open(io.BytesIO(enhanced_image_content))
        st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)
        st.success("Imagen mejorada con éxito")
        st.button(f" [Download Enhanced Image]({output_url})")


# import streamlit as st
# import base64
# import hashlib
# from time import sleep
# from PIL import Image
# import httpx
# import io  # Importar la biblioteca io
# import os
# from dotenv import load_dotenv

# API_KEY = os.getenv("REMINI_API_KEY")
# BASE_URL = "https://developer.remini.ai/api"

# load_dotenv()

# def enhance_image(file_content):
#     image_md5, content = _get_image_md5_content(file_content)
    
#     with httpx.Client(
#         base_url=BASE_URL,
#         headers={"Authorization": f"Bearer {API_KEY}"},
#     ) as client:
#         response = client.post(
#             "/tasks",
#             json={
#                 "tools": [
#                     {"type": "face_enhance", "mode": "beautify"},
#                     {"type": "background_enhance", "mode": "base"}
#                 ],
#                 "image_md5": image_md5,
#                 "image_content_type": "image/jpeg",
#                 "output_content_type": "image/jpeg"
#             }
#         )
#         assert response.status_code == 200
#         body = response.json()
#         task_id = body["task_id"]

#         response = httpx.put(
#             body["upload_url"], headers=body["upload_headers"],
#             content=content, timeout=60
#         )
#         assert response.status_code == 200

#         response = client.post(f"/tasks/{task_id}/process")
#         assert response.status_code == 202

#         for i in range(50):
#             response = client.get(f"/tasks/{task_id}")
#             assert response.status_code == 200

#             if response.json()["status"] == "completed":
#                 break
#             else:
#                 sleep(2)

#         return response.json()["result"]["output_url"]

# def _get_image_md5_content(file_content):
#     content = file_content.read()
#     image_md5 = base64.b64encode(hashlib.md5(content).digest()).decode("utf-8")
#     return image_md5, content

# st.title("Mejorar imagen con Remini")
# st.caption("🚀 Este filtro es excluivamene para blacks")
# st.caption("🚀 No te ofendas si no funciona contigo")

# uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg"])

# if uploaded_file:
#     st.image(uploaded_file, caption="Imagen cargada", use_column_width=True)
    
#     if st.button("Mejorar imagen"):
#         st.text("Mejorando imagen. Please wait...")
#         output_url = enhance_image(uploaded_file)
        
#         enhanced_image_content = httpx.get(output_url).content
#         enhanced_image = Image.open(io.BytesIO(enhanced_image_content))
#         st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)
#         st.success("Imagen mejorada con éxito")
#         st.button(f" [Download Enhanced Image]({output_url})")


# import streamlit as st
# import base64
# import hashlib
# from time import sleep
# import httpx
# import os
# from dotenv import load_dotenv

# API_KEY = os.getenv("REMINI_API_KEY")
# BASE_URL = "https://developer.remini.ai/api"

# load_dotenv()

# def enhance_image(file_content):
#     image_md5, content = _get_image_md5_content(file_content)
    
#     with httpx.Client(
#         base_url=BASE_URL,
#         headers={"Authorization": f"Bearer {API_KEY}"},
#     ) as client:
#         response = client.post(
#             "/tasks",
#             json={
#                 "tools": [
#                     {"type": "face_enhance", "mode": "beautify"},
#                     {"type": "background_enhance", "mode": "base"}
#                 ],
#                 "image_md5": image_md5,
#                 "image_content_type": "image/jpeg",
#                 "output_content_type": "image/jpeg"
#             }
#         )
#         assert response.status_code == 200
#         body = response.json()
#         task_id = body["task_id"]

#         response = httpx.put(
#             body["upload_url"], headers=body["upload_headers"],
#             content=content, timeout=60
#         )
#         assert response.status_code == 200

#         response = client.post(f"/tasks/{task_id}/process")
#         assert response.status_code == 202

#         for i in range(50):
#             response = client.get(f"/tasks/{task_id}")
#             assert response.status_code == 200

#             if response.json()["status"] == "completed":
#                 break
#             else:
#                 sleep(2)

#         return response.json()["result"]["output_url"]

# def _get_image_md5_content(file_content):
#     content = file_content.read()
#     image_md5 = base64.b64encode(hashlib.md5(content).digest()).decode("utf-8")
#     return image_md5, content

# st.title("Remini Image Enhancement")

# uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg"])

# if uploaded_file:
#     st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
#     if st.button("Enhance Image"):
#         st.text("Enhancing image. Please wait...")
#         output_url = enhance_image(uploaded_file)
#         st.success(f"Image enhanced successfully! [Download Enhanced Image]({output_url})")
