import numpy as np
import streamlit as st
from sklearn.cluster import KMeans
import cv2
from PIL import Image
import io
import base64


def get_image_download_link(img, filename, text):
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:image/jpeg;base64,{img_str}" download="{filename}">{text}</a>'
    return href


def process_image(image, n_colors):
    image = np.array(image)
    image = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(image)

    def recreate_image(codebook, labels, w, h):
        d = codebook.shape[1]
        image = np.zeros((w, h, d))
        label_idx = 0
        for i in range(w):
            for j in range(h):
                image[i][j] = codebook[labels[label_idx]]
                label_idx += 1
        return image

    labels = kmeans.predict(image)
    w, h = image.shape[:2]
    canvas = recreate_image(kmeans.cluster_centers_, labels, w, h)
    return canvas


st.title('Gerador de pintura por números')
st.write('Por favor, carregue sua imagem abaixo:')

uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem carregada.', use_column_width=True)

    n_colors = st.slider('Selecione o número de cores', 1, 20, 3)

    if st.button('Gerar pintura por números'):
        try:
            canvas = process_image(image, n_colors)
            st.image(canvas, caption='Sua pintura por números.', use_column_width=True)

            result = Image.fromarray((canvas * 255).astype(np.uint8))
            st.markdown(get_image_download_link(result, 'pintura_por_numeros.png', 'Clique aqui para baixar a imagem'), unsafe_allow_html=True)
        except Exception as e:
            st.error(f'Ocorreu um erro ao processar a imagem: {e}')
else:
    st.error('Por favor, carregue uma imagem.')

