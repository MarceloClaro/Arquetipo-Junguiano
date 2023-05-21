import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sklearn.cluster import KMeans



# Dicionário com cores da psicologia das cores
cores_junguianas = {
    'Vermelho': {'Características': '...', 'Diagnósticos': '...'},
    'Azul': {'Características': '...', 'Diagnósticos': '...'},
    'Amarelo': {'Características': '...', 'Diagnósticos': '...'}
}

class Canvas:
    def __init__(self, image, num_cores, pixel_size):
        self.image = image
        self.num_cores = num_cores
        self.pixel_size = pixel_size
        self.result_image = None
        self.segmented_image = None
        self.colors = None
        self.color_areas = None

    def generate(self):
        # Lógica para gerar a imagem resultante, as cores e a imagem segmentada
        height, width, _ = self.image.shape
        self.result_image = np.zeros((height, width, 3), dtype=np.uint8)
        self.segmented_image = np.zeros((height, width), dtype=np.uint8)
        self.colors = []
        self.color_areas = []

        # Converter a imagem para o formato RGB
        image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        # Converter a imagem para o formato LAB
        image_lab = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2LAB)

        # Aplicar segmentação de cor K-means
        pixels = image_lab.reshape((-1, 3))
        kmeans = KMeans(n_clusters=self.num_cores, random_state=0).fit(pixels)
        segmented_labels = kmeans.predict(pixels)

        # Obter as cores e áreas correspondentes
        for i in range(self.num_cores):
            color = kmeans.cluster_centers_[i].astype(int)
            area = np.sum(segmented_labels == i)

            self.colors.append(color)
            self.color_areas.append(area)

        # Pintar a imagem resultante com as cores correspondentes
        for i in range(height):
            for j in range(width):
                pixel_lab = image_lab[i, j]
                label = kmeans.predict([pixel_lab])[0]
                self.result_image[i, j] = kmeans.cluster_centers_[label]

        # Atualizar a imagem segmentada
        self.segmented_image = segmented_labels.reshape((height, width))

        return self.result_image, self.segmented_image, self.colors, self.color_areas



def convert_image(image):
    img_array = np.array(image)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    return img_array

def calculate_ink_quantities(colors, total_ink):
    # Cálculo das quantidades de tinta em ml de cada cor primária (C, M, Y, K)
    ink_quantities = []

    # ...
    # Implemente a lógica para calcular as quantidades de tinta em ml de cada cor primária
    # ...

    return ink_quantities

def find_nearest_color(palette_color):
    # Lógica para buscar a cor mais próxima no dicionário "cores_junguianas"
    nearest_color = None

    # ...
    # Implemente a lógica para buscar a cor mais próxima no dicionário "cores_junguianas"
    # ...

    return nearest_color

def image_to_base64(image):
    # Converte uma imagem em formato numpy para base64
    pil_image = Image.fromarray(image)
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def main():
    st.title("Aplicativo de Pintura por Números")

    # Etapa 1: Carregamento da imagem
    st.header("1. Carregamento da Imagem")
    uploaded_image = st.file_uploader("Carregue uma imagem", type=['png', 'jpg', 'jpeg'])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Imagem carregada", use_column_width=True)

        # Etapa 2: Conversão da imagem
        st.header("2. Conversão da Imagem")
        img_array = convert_image(image)

        # Etapa 3: Escolha do número de cores
        st.header("3. Escolha do Número de Cores")
        num_cores = st.slider("Selecione o número de cores", min_value=2, max_value=10, value=5, step=1)

        # Etapa 4: Escolha do total em ml da tinta
        st.header("4. Escolha do Total de Tinta")
        total_ink = st.slider("Selecione o total de tinta em ml", min_value=10, max_value=100, value=50, step=10)

        # Etapa 5: Escolha do tamanho do pixel
        st.header("5. Escolha do Tamanho do Pixel")
        pixel_size = st.slider("Selecione o tamanho do pixel", min_value=5, max_value=20, value=10, step=1)

        # Etapa 6: Geração da paleta de cores, imagem segmentada e porcentagem de cada cor
        st.header("6. Geração da Paleta de Cores e Imagem Segmentada")
        canvas = Canvas(img_array, num_cores, pixel_size)
        result_image, segmented_image, colors, color_areas = canvas.generate()

        # Etapa 7: Exibição das imagens
        st.header("7. Exibição das Imagens")
        st.subheader("Imagem Resultante")
        st.image(result_image, caption="Imagem resultante", use_column_width=True)
        st.subheader("Imagem Segmentada")
        st.image(segmented_image, caption="Imagem segmentada", use_column_width=True)

        # Etapa 8: Cálculo das quantidades de tinta e áreas das cores
        st.header("8. Cálculo das Quantidades de Tinta e Áreas das Cores")
        ink_quantities = calculate_ink_quantities(colors, total_ink)
        for i, color in enumerate(colors):
            st.write(f"Cor: {color}")
            st.write(f"Dosagem de tinta (ml): {ink_quantities[i]}")
            st.write(f"Área correspondente na imagem (pixels): {color_areas[i]}")

        # Etapa 9: Busca da cor mais próxima
        st.header("9. Busca da Cor Mais Próxima")
        for color in colors:
            nearest_color = find_nearest_color(color)
            st.write(f"Cor da paleta: {color}")
            st.write(f"Cor mais próxima: {nearest_color}")
            st.write(f"Características: {cores_junguianas[nearest_color]['Características']}")
            st.write(f"Diagnósticos: {cores_junguianas[nearest_color]['Diagnósticos']}")

        # Etapa 10: Exibição das informações da paleta de cores
        st.header("10. Informações da Paleta de Cores")
        for i, color in enumerate(colors):
            st.write(f"Cor: {color}")
            st.write(f"Dosagem de tinta (ml): {ink_quantities[i]}")
            st.write(f"Área correspondente na imagem (pixels): {color_areas[i]}")
            st.write(f"Características: {cores_junguianas[color]['Características']}")
            st.write(f"Diagnósticos: {cores_junguianas[color]['Diagnósticos']}")

        # Etapa 11: Download das imagens
        st.header("11. Download das Imagens")
        st.write("Clique nos links abaixo para fazer o download das imagens:")
        st.markdown(f"[Imagem Resultante](data:image/jpeg;base64,{image_to_base64(result_image)})")
        st.markdown(f"[Imagem Segmentada](data:image/jpeg;base64,{image_to_base64(segmented_image)})")

if __name__ == '__main__':
    main()
