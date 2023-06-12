import streamlit as st
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from scipy.spatial import distance

# Função para encontrar a cor mais próxima no dicionário
def encontrar_cor_mais_proxima(rgb):
    cor_mais_proxima = None
    menor_distancia = float('inf')

    for chave, valor in cores_junguianas.items():
        distancia_cor = distance.euclidean(rgb, valor['rgb'])
        if distancia_cor < menor_distancia:
            menor_distancia = distancia_cor
            cor_mais_proxima = valor

    return cor_mais_proxima

# Carregar o dicionário com as cores junguianas
cores_junguianas = {
    # Seu dicionário de cores aqui...
}

# Configurações do aplicativo Streamlit
st.image("clube.png")  # Adiciona a imagem no topo do app
st.title("Análise de Cor Dominante das Pinturas de Telas")
st.write("""
Este aplicativo é usado para analisar a cor dominante em uma pintura e encontrar sua correspondência em um dicionário de cores com significados.

Em resumo, este aplicativo pode ajudar a revelar os significados ocultos nas cores usadas em obras de arte.
""")
st.write("Carregue uma imagem e descubra a cor dominante e sua correspondência no dicionário de cores junguianas.")

# Carregar a imagem
imagem = st.file_uploader("Selecione uma imagem", type=['jpg', 'jpeg', 'png'])

if imagem is not None:
    # Exibir a imagem carregada
    imagem_pil = Image.open(imagem)
    st.image(imagem_pil, caption="Imagem Original", use_column_width=True)

    # Converter a imagem para um array numpy
    imagem_array = np.array(imagem_pil)

    # Redimensionar a imagem para 100x100 pixels
    imagem_redimensionada = np.array(imagem_pil.resize((100, 100)))

    # Obter os pixels da imagem redimensionada
    pixels = imagem_redimensionada.reshape(-1, 3)

    # Realizar a clusterização dos pixels
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(pixels)

    # Encontrar a cor dominante
    cor_dominante = kmeans.cluster_centers_[kmeans.labels_].mean(axis=0).astype(int)

    # Encontrar a cor mais próxima no dicionário
    cor_proxima = encontrar_cor_mais_proxima(cor_dominante)
    
    # Exibir a cor dominante e sua correspondência no dicionário
    st.subheader("Resultado")
    st.write(f"Cor Dominante: RGB {cor_dominante}")
    st.write(f"Cor Correspondente no Dicionário: {cor_proxima['cor']}")
    st.write(f"Anima/Animico: {cor_proxima['anima_animico']}")
    st.write(f"Sombra: {cor_proxima['sombra']}")
    st.write(f"Personalidade: {cor_proxima['personalidade']}")
    st.write(f"Diagnóstico: {cor_proxima['diagnostico']}")
    
    # Exibir a imagem segmentada do cluster
    imagem_segmentada = cor_dominante.reshape(1, 1, 3)
    st.image(imagem_segmentada, caption="Imagem Segmentada do Cluster", use_column_width=True)

    # Variáveis do usuárioDesculpe-me pela interrupção, aqui está a continuação do código:

```python
    # Variáveis do usuário
    animico = st.slider("Anímico", 0.0, 100.0, (cor_proxima['anima_animico']))
    sombra = st.slider("Sombra", 0.0, 100.0, (cor_proxima['sombra']))
    personalidade = st.slider("Personalidade", 0.0, 100.0, (cor_proxima['personalidade']))
    diagnostico = st.slider("Diagnóstico", 0.0, 100.0, (cor_proxima['diagnostico']))

    # Exibir os resultados do usuário
    st.subheader("Resultados do Usuário")
    st.write(f"Anima/Animico: {animico}")
    st.write(f"Sombra: {sombra}")
    st.write(f"Personalidade: {personalidade}")
    st.write(f"Diagnóstico: {diagnostico}")
