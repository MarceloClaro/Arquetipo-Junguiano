import numpy as np  
import cv2  
from sklearn.cluster import KMeans  
from sklearn.utils import shuffle  
import streamlit as st  
from PIL import Image  
import io  


class Canvas():
    def __init__(self, src, nb_color, pixel_size=4000):
        self.src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  
        self.nb_color = nb_color
        self.tar_width = pixel_size
        self.colormap = []

    def generate(self):
        # Métodos aplicados na imagem
        im_source = self.resize()
        clean_img = self.cleaning(im_source)
        width, height, depth = clean_img.shape
        clean_img = np.array(clean_img, dtype="uint8") / 255
        quantified_image, colors = self.quantification(clean_img)
        canvas = np.ones(quantified_image.shape[:2], dtype="uint8") * 255

        # Encontrando contornos e aplicando texto
        for ind, color in enumerate(colors):
            self.colormap.append([int(c * 255) for c in color])
            mask = cv2.inRange(quantified_image, color, color)
            cnts = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]

            for contour in cnts:
                _, _, width_ctr, height_ctr = cv2.boundingRect(contour)
                if width_ctr > 10 and height_ctr > 10 and cv2.contourArea(contour, True) < -100:
                    cv2.drawContours(canvas, [contour], -1, (0, 0, 0), 1)
                    txt_x, txt_y = contour[0][0]
                    cv2.putText(canvas, '{:d}'.format(ind + 1), (txt_x, txt_y + 15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

        return canvas, colors, quantified_image

    def resize(self):
        (height, width) = self.src.shape[:2]
        if height > width:  # modo retrato
            dim = (int(width * self.tar_width / float(height)), self.tar_width)
        else:
            dim = (self.tar_width, int(height * self.tar_width / float(width)))
        return cv2.resize(self.src, dim, interpolation=cv2.INTER_AREA)

    def cleaning(self, picture):
        clean_pic = cv2.fastNlMeansDenoisingColored(picture, None, 10, 10, 7, 21)
        kernel = np.ones((5, 5), np.uint8)
        img_erosion = cv2.erode(clean_pic, kernel, iterations=1)
        img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
        return img_dilation

    def quantification(self, picture):
        width, height, depth = picture.shape
        flattened = np.reshape(picture, (width * height, depth))
        sample = shuffle(flattened)[:1000]
        kmeans = KMeans(n_clusters=self.nb_color).fit(sample)
        labels = kmeans.predict(flattened)
        new_img = self.recreate_image(kmeans.cluster_centers_, labels, width, height)
        return new_img, kmeans.cluster_centers_

    def recreate_image(self, codebook, labels, width, height):
        vfunc = np.vectorize(lambda label: codebook[label])
        new_img = vfunc(labels)
        new_img = np.reshape(new_img, (width, height, codebook.shape[1]))
        return new_img


def find_nearest_color(input_color, color_dict):
    # Convertendo a cor de entrada para Lab
    input_color = np.uint8([[input_color]])
    input_color = cv2.cvtColor(input_color, cv2.COLOR_RGB2LAB)

    min_distance = float('inf')
    nearest_color_name = None
    nearest_color_value = None

    # Percorrendo o dicionário de cores
    for color_name, color_value in color_dict.items():
        # Convertendo a cor do dicionário para Lab
        dict_color = np.uint8([[color_value]])
        dict_color = cv2.cvtColor(dict_color, cv2.COLOR_RGB2LAB)

        # Calculando a distância euclidiana
        distance = cv2.norm(input_color, dict_color)

        # Verificando se a distância é a menor encontrada até agora
        if distance < min_distance:
            min_distance = distance
            nearest_color_name = color_name
            nearest_color_value = color_value

    return nearest_color_name, nearest_color_value


# Dicionário de cores dos arquétipos junguianos
jung_colors = {
    'Anima/Animus': [255, 0, 0],  # Exemplo: vermelho
    'Sombra': [0, 255, 0],  # Exemplo: verde
    'Personalidade': [0, 0, 255]  # Exemplo: azul
}

# Upload da imagem
uploaded_file = st.file_uploader("Escolha uma imagem...", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Realizando a análise de cores
    colors_analysis = Canvas(np.array(image), 5)
    img_canvas, colors, img_quantified = colors_analysis.generate()

    # Encontrando a cor mais próxima para cada cor encontrada na imagem
    for i, color in enumerate(colors):
        color_rgb = [int(c * 255) for c in color]
        nearest_color_name, nearest_color_value = find_nearest_color(color_rgb, jung_colors)

        st.write(f'Cor {i+1} mais próxima no dicionário de cores dos arquétipos junguianos: {nearest_color_name} ({nearest_color_value})')
