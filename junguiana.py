import streamlit as st
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

class Canvas:
    def __init__(self, src, nb_color, pixel_size):
        self.src = src.convert("RGB")
        self.nb_color = nb_color
        self.pixel_size = pixel_size

    def resize(self):
        width, height = self.src.size
        new_height = self.pixel_size
        new_width = int(new_height * width / height)
        self.src = self.src.resize((new_width, new_height))

    def cleaning(self):
        # Implementação da limpeza da imagem
        pass

    def quantification(self):
        # Convertendo a imagem para um array NumPy
        self.image_array = np.array(self.src)

        # Redimensionando a matriz para ter apenas duas dimensões
        self.image_array = self.image_array.reshape((-1, 3))

        # Clusterizando a imagem usando K-means
        self.kmeans = KMeans(n_clusters=self.nb_color)
        self.labels = self.kmeans.fit_predict(self.image_array)

        # Calculando a porcentagem de pixels em cada cluster
        self.counts = np.bincount(self.labels)
        self.percentages = self.counts / len(self.labels)

    def recreate_image(self):
        # Substituindo cada pixel pelo centro do cluster correspondente
        self.quantified_image = self.kmeans.cluster_centers_[self.labels].astype(int)

        # Redimensionando a matriz de volta para o formato de imagem
        self.quantified_image = self.quantified_image.reshape(self.src.size[1], self.src.size[0], 3)

        # Convertendo a matriz de volta para uma imagem
        self.quantified_image = Image.fromarray(self.quantified_image)

    def generate(self):
        self.resize()
        self.cleaning()
        self.quantification()
        self.recreate_image()

    def display(self):
        st.image(self.quantified_image)
        for i in range(self.nb_color):
            rgb = self.kmeans.cluster_centers_[i].astype(int)
            st.write(f"Cluster {i+1}: {self.percentages[i]*100:.2f}%  RGB:{rgb}")
            
            fig, ax = plt.subplots(figsize=(2, 2))
            ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=rgb/255))
            plt.axis('off')
            st.pyplot(fig)

def main():
    st.title("Análise de Cores de Imagem")

    uploaded_file = st.file_uploader("Carregue uma imagem", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagem Original.', use_column_width=True)

        n_clusters = st.slider("Número de clusters", min_value=2, max_value=10, value=5)
        pixel_size = st.slider("Tamanho do Pixel", min_value=10, max_value=300, value=100)

        if st.button('Processar Imagem'):
            canvas = Canvas(image, n_clusters, pixel_size)
            canvas.generate()
            canvas.display()

if __name__ == '__main__':
    main()
