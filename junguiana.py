import streamlit as st
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

def process_image(image):
    # Converter a imagem para RGB
    image = image.convert('RGB')
    
    # Redimensionar a imagem para um tamanho padrão para acelerar a clusterização
    image = image.resize((100, 100))
    
    # Converter a imagem em uma matriz NumPy
    image_array = np.array(image)
    
    # Redimensionar a matriz para ter apenas duas dimensões
    image_array = image_array.reshape((-1, 3))
    
    return image_array

def clusterize_image(image_array, n_clusters):
    # Clusterizar a imagem usando K-means
    kmeans = KMeans(n_clusters=n_clusters)
    labels = kmeans.fit_predict(image_array)
    
    # Contar a porcentagem de pixels em cada cluster
    counts = np.bincount(labels)
    percentages = counts / len(labels)
    
    return percentages

st.title("Clusterização de Imagem RGB")

# Permitir que o usuário faça upload de uma imagem
uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg"])

if uploaded_file is not None:
    # Carregar a imagem
    image = Image.open(uploaded_file)
    
    # Processar a imagem
    image_array = process_image(image)
    
    # Permitir que o usuário escolha o número de clusters
    n_clusters = st.slider("Número de clusters", min_value=2, max_value=10, value=5)
    
    # Clusterizar a imagem
    percentages = clusterize_image(image_array, n_clusters)
    
    # Exibir as porcentagens
    for i in range(n_clusters):
        st.write(f"Cluster {i+1}: {percentages[i]*100:.2f}%")
