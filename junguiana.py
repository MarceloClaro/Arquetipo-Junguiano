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
    '1': {
        'cor': 'Vermelho Vivo',
        'rgb': (255, 0, 0),
        'anima_animico': 'Vitalidade',
        'sombra': 'Impulsividade',
        'personalidade': 'Autocontrole',
        'diagnostico': 'No processo de pintura de tela, o Vermelho Vivo representa uma expressão intensa de energia e paixão. Sua mensagem é de vitalidade e autenticidade, encorajando a expressão livre de emoções.'
    },
    '2': {
        'cor': 'Rosa Brilhante',
        'rgb': (255, 105, 180),
        'anima_animico': 'Abundância',
        'sombra': 'Propensão ao Excesso',
        'personalidade': 'Equilíbrio',
        'diagnostico': 'Ao pintar com o Rosa Brilhante, você traz uma sensação de abundância e gratidão à sua tela. A mensagem transmitida por essa cor é de equilíbrio emocional e alegria na expressão artística.'
    },
    '3': {
        'cor': 'Laranja Ardente',
        'rgb': (255, 140, 0),
        'anima_animico': 'Entusiasmo',
        'sombra': 'Imaturidade',
        'personalidade': 'Sabedoria',
        'diagnostico': 'A cor Laranja Ardente em seu processo de pintura representa entusiasmo e criatividade vibrantes. Ela convida você a abraçar sua criança interior e expressar-se com alegria e sabedoria.'
    },
    '4': {
        'cor': 'Magenta Vibrante',
        'rgb': (255, 0, 255),
        'anima_animico': 'Criatividade',
        'sombra': 'Contrariedade',
        'personalidade': 'Flexibilidade',
        'diagnostico': 'Quando você pinta com Magenta Vibrante, está canalizando sua criatividade e expressão artística única. Essa cor traz uma mensagem de flexibilidade e adaptabilidade diante dos desafios.'
    },
    '5': {
        'cor': 'Índigo Profundo',
        'rgb': (75, 0, 130),
        'anima_animico': 'Intuição',
        'sombra': 'Dúvida',
        'personalidade': 'Inteligência',
        'diagnostico': 'O Índigo Profundo em sua tela reflete uma conexão profunda com sua intuição e sabedoria interior. Essa cor carrega uma mensagem de confiança e inteligência na manifestação de sua expressão artística.'
    },
    '6': {
        'cor': 'Verde Claro',
        'rgb': (0, 255, 0),
        'anima_animico': 'Renovação',
        'sombra': 'Insegurança',
        'personalidade': 'Autoconfiança',
        'diagnostico': 'Quando você pinta com Verde Claro, está trazendo uma sensação de renovação e crescimento à sua expressão artística. Essa cor transmite uma mensagem de autoconfiança, encorajando você a se expressar livremente e acreditar em seu próprio potencial criativo.'
    },
    '7': {
        'cor': 'Azul Elétrico',
        'rgb': (0, 0, 255),
        'anima_animico': 'Liberdade',
        'sombra': 'Desordem',
        'personalidade': 'Responsabilidade',
        'diagnostico': 'Ao utilizar o Azul Elétrico em suas telas, você expressa uma sensação de liberdade e expansão. Essa cor transmite a mensagem de equilíbrio entre a liberdade criativa e a responsabilidade de moldar sua expressão artística de forma consciente.'
    },
    '8': {
        'cor': 'Amarelo Solar',
        'rgb': (255, 255, 0),
        'anima_animico': 'Otimismo',
        'sombra': 'Negatividade',
        'personalidade': 'Intencionalidade',
        'diagnostico': 'O Amarelo Solar em sua pintura traz uma energia otimista e iluminada. Sua mensagem é de positividade e intencionalidade, convidando-o a expressar sua arte com alegria e propósito.'
    },
    '9': {
        'cor': 'Lilás Suave',
        'rgb': (204, 153, 255),
        'anima_animico': 'Humildade',
        'sombra': 'Inadaptabilidade',
        'personalidade': 'Adaptabilidade',
        'diagnostico': 'Ao utilizar o Lilás Suave em suas telas, você traz uma sensação de humildade e suavidade à sua expressão artística. Essa cor carrega a mensagem de adaptabilidade e abertura às transformações que ocorrem durante o processo de pintura.'
    },
    '10': {
        'cor': 'Castanho Neutro',
        'rgb': (139, 69, 19),
        'anima_animico': 'Estabilidade',
        'sombra': 'Estagnação',
        'personalidade': 'Evolução',
        'diagnostico': 'A cor Castanho Neutro em sua pintura representa uma sensação de estabilidade e segurança. Sua mensagem é de evolução contínua, incentivando a busca por novas perspectivas e o crescimento artístico.'
    },
    '11': {
        'cor': 'Turquesa Brilhante',
        'rgb': (0, 255, 255),
        'anima_animico': 'Energia',
        'sombra': 'Impaciência',
        'personalidade': 'Paciência',
        'diagnostico': 'Quando você pinta com Turquesa Brilhante, está trazendo uma energia vibrante e estimulante à sua tela. Essa cor transmite uma mensagem de equilíbrio entre a energia criativa e a paciência necessária para desenvolver sua expressão artística de forma completa e satisfatória.'
    },
    '12': {
        'cor': 'Cinza Algo',
        'rgb': (128, 128, 128),
        'anima_animico': 'Introversão',
        'sombra': 'Desalinho',
        'personalidade': 'Clareza',
        'diagnostico': 'Ao utilizar o Cinza Algo em suas telas, você traz uma atmosfera de introspecção e reflexão. Essa cor carrega a mensagem de encontrar clareza e foco em meio à desordem, incentivando uma expressão artística alinhada com sua verdade interior.'
    },
    '13': {
        'cor': 'Branco Radiante',
        'rgb': (255, 255, 255),
        'anima_animico': 'Pureza',
        'sombra': 'Falsidade',
        'personalidade': 'Honradez',
        'diagnostico': 'O Branco Radiante em seu processo de pintura representa pureza e autenticidade. Sua mensagem é de honradez na expressão artística, encorajando você a pintar com sinceridade e verdade, evitando qualquer falsidade.'
    },
    '14': {
        'cor': 'Azul Escuro',
        'rgb': (0, 0, 128),
        'anima_animico': 'Segurança',
        'sombra': 'Desconfiança',
        'personalidade': 'Tranquilidade',
        'diagnostico': 'Ao utilizar o Azul Escuro em suas telas, você transmite uma sensação de segurança e tranquilidade. Essa cor carrega a mensagem de confiança na expressão artística, permitindo-se mergulhar nas profundezas da criatividade com confiança e serenidade.'
    },
    '15': {
        'cor': 'Verde Escuro',
        'rgb': (0, 100, 0),
        'anima_animico': 'Estoicismo',
        'sombra': 'Frialdade',
        'personalidade': 'Afetuosidade',
        'diagnostico': 'Quando você pinta com Verde Escuro, está explorando um senso de estoicismo e serenidade em sua expressão artística. Essa cor transmite a mensagem de equilibrar a frieza com a afetuosidade, resultando em obras cheias de serenidade e profundidade emocional.'
    },
    '16': {
        'cor': 'Laranja Avermelhado',
        'rgb': (255, 69, 0),
        'anima_animico': 'Envolvimento',
        'sombra': 'Insegurança',
        'personalidade': 'Confiança',
        'diagnostico': 'Ao utilizar o Laranja Avermelhado em suas telas, você traz um senso de envolvimento e paixão à sua expressão artística. Essa cor transmite uma mensagem de confiança em si mesmo, encorajando-o a se entregar completamente ao processo criativo e expressar suas emoções e ideias sem medo ou insegurança.'
    },
    '17': {
        'cor': 'Rosa Calorosa',
        'rgb': (255, 192, 203),
        'anima_animico': 'Carinho',
        'sombra': 'Medo',
        'personalidade': 'Coragem',
        'diagnostico': 'Ao pintar com Rosa Calorosa, você traz uma energia de carinho e amor à sua tela. Essa cor carrega a mensagem de coragem, convidando-o a se expressar de forma amorosa e gentil através de sua arte, superando qualquer medo que possa surgir.'
    },
    '18': {
        'cor': 'Vermelho Oculto',
        'rgb': (139, 0, 0),
        'anima_animico': 'Força',
        'sombra': 'Ira',
        'personalidade': 'Autocontrole',
        'diagnostico': 'Quando você utiliza o Vermelho Oculto em suas telas, traz à tona uma energia poderosa e intensa. Sua mensagem é de força interior e autocontrole, incentivando você a expressar suas emoções com equilíbrio e assertividade, evitando ser dominado pela ira.'
    },
    '19': {
        'cor': 'Magenta Escuro',
        'rgb': (139, 0, 139),
        'anima_animico': 'Profundidade',
        'sombra': 'Desespero',
        'personalidade': 'Esperança',
        'diagnostico': 'Ao pintar com Magenta Escuro, você explora as camadas mais profundas de emoção em sua arte. Essa cor carrega a mensagem de encontrar esperança e significado mesmo nas situações mais desafiadoras, superando o desespero e permitindo que a esperança brilhe.'
    },
    '20': {
        'cor': 'Índigo Vintage',
        'rgb': (75, 0, 130),
        'anima_animico': 'Consciência',
        'sombra': 'Desesperança',
        'personalidade': 'Fé',
        'diagnostico': 'Ao utilizar o Índigo Vintage em suas telas, você evoca uma consciência profunda e espiritual em sua expressão artística. Essa cor transmite a mensagem de fé e confiança no processo criativo, inspirando-o a pintar com significado e propósito, mesmo em momentos de desesperança.'
    },
    '21': {
        'cor': 'Verde Menta',
        'rgb': (152, 251, 152),
        'anima_animico': 'Calma',
        'sombra': 'Desânimo',
        'personalidade': 'Perseverança',
        'diagnostico': 'Quando você pinta com Verde Menta, traz uma sensação de calma e tranquilidade à sua expressão artística. Essa cor transmite a mensagem de perseverança, incentivando você a persistir em sua jornada artística mesmo diante dos desafios e momentos de desânimo.'
    },
    '22': {
        'cor': 'Azul Petróleo',
        'rgb': (0, 128, 128),
        'anima_animico': 'Liderança',
        'sombra': 'Rigidez',
        'personalidade': 'Suavidade',
        'diagnostico': 'Ao utilizar o Azul Petróleo em suas telas, você evoca uma energia de liderança e autoridade na sua expressão artística. Essa cor carrega a mensagem de suavidade e flexibilidade, incentivando uma abordagem harmoniosa e receptiva em sua arte.'
    },
    '23': {
        'cor': 'Amarelo Luminoso',
        'rgb': (255, 255, 102),
        'anima_animico': 'Alegria',
        'sombra': 'Ansiedade',
        'personalidade': 'Autogoverno',
        'diagnostico': 'Quando você pinta com Amarelo Luminoso, está trazendo uma energia de alegria e otimismo à sua tela. Essa cor transmite a mensagem de autogoverno, convidando-o a expressar sua arte com confiança e leveza, superando a ansiedade.'
    },
    '24': {
        'cor': 'Lilás Atrevido',
        'rgb': (153, 50, 204),
        'anima_animico': 'Intriga',
        'sombra': 'Preconceito',
        'personalidade': 'Respeito',
        'diagnostico': 'Ao utilizar o Lilás Atrevido em suas telas, você traz uma sensação de intriga e curiosidade à sua expressão artística. Essa cor carrega a mensagem de respeito, incentivando-o a abraçar a diversidade e a explorar diferentes perspectivas em sua arte.'
    },
    '25': {
        'cor': 'Marrom Neutro',
        'rgb': (139, 69, 19),
        'anima_animico': 'Praticidade',
        'sombra': 'Comodismo',
        'personalidade': 'Determinação',
        'diagnostico': 'Ao utilizar o Marrom Neutro em suas telas, você traz uma sensação de praticidade e estabilidade à sua expressão artística. Essa cor carrega a mensagem de determinação, convidando-o a se comprometer com seu processo criativo e superar o comodismo.'
    },
    '26': {
        'cor': 'Turquesa Refinado',
        'rgb': (64, 224, 208),
        'anima_animico': 'Gratidão',
        'sombra': 'Resentimento',
        'personalidade': 'Agradecimento',
        'diagnostico': 'Ao pintar com Turquesa Refinado, você expressa uma profunda gratidão em sua arte. Essa cor transmite a mensagem de agradecimento, convidando-o a apreciar e valorizar o processo criativo, superando qualquer sentimento de ressentimento.'
    },
    '27': {
        'cor': 'Cinza Confiante',
        'rgb': (128, 128, 128),
        'anima_animico': 'Resiliência',
        'sombra': 'Hiperestimulação',
        'personalidade': 'Autorespeito',
        'diagnostico': 'Ao utilizar o Cinza Confiante em suas telas, você evoca uma energia de resiliência e autodeterminação em sua expressão artística. Essa cor carrega a mensagem de autorespeito, incentivando-o a cuidar de si mesmo e a encontrar um equilíbrio saudável em seu processo criativo.'
    },
    '28': {
        'cor': 'Branco Clássico',
        'rgb': (245, 245, 245),
        'anima_animico': 'Simplicidade',
        'sombra': 'Conformismo',
        'personalidade': 'Inovação',
        'diagnostico': 'Ao utilizar o Branco Clássico em suas telas, você traz uma sensação de simplicidade e pureza à sua expressão artística. Essa cor carrega a mensagem de inovação, convidando-o a explorar novas ideias e abordagens criativas em seu trabalho.'
    },
    '29': {
        'cor': 'Azul Marinho',
        'rgb': (0, 0, 128),
        'anima_animico': 'Iniciativa',
        'sombra': 'Intransigência',
        'personalidade': 'Aceitação',
        'diagnostico': 'Quando você pinta com Azul Marinho, está trazendo uma energia de iniciativa e determinação à sua tela. Essa cor transmite a mensagem de aceitação, incentivando-o a abraçar diferentes perspectivas e a ser receptivo às mudanças em seu processo criativo.'
    },
    '30': {
        'cor': 'Verde Vinho',
        'rgb': (128, 0, 0),
        'anima_animico': 'Experiência',
        'sombra': 'Ira reprimida',
        'personalidade': 'Autocura',
        'diagnostico': 'Ao utilizar o Verde Vinho em suas telas, você traz uma energia de experiência e transformação à sua expressão artística. Essa cor carrega a mensagem de autocura, convidando-o a explorar e liberar qualquer raiva reprimida por meio da arte.'
    },
    '31': {
        'cor': 'Pêssego Radiante',
        'rgb': (255, 204, 153),
        'anima_animico': 'Amizade',
        'sombra': 'Autossabotagem',
        'personalidade': 'Autocuidado',
        'diagnostico': 'Ao pintar com Pêssego Radiante, você traz uma energia de amizade e conexão à sua arte. Essa cor carrega a mensagem de autocuidado, convidando-o a cultivar um relacionamento saudável consigo mesmo e a evitar autossabotagem em seu processo criativo.'
    },
    '32': {
        'cor': 'Rosa Neutro',
        'rgb': (205, 183, 181),
        'anima_animico': 'Compaixão',
        'sombra': 'Submissão',
        'personalidade': 'Autonomia',
        'diagnostico': 'Ao utilizar o Rosa Neutro em suas telas, você evoca uma energia de compaixão e empatia em sua expressão artística. Essa cor transmite a mensagem de autonomia, incentivando-o a se expressar com autenticidade e a estabelecer limites saudáveis em seu trabalho.'
    },
    '33': {
        'cor': 'Vermelho Real',
        'rgb': (227, 38, 54),
        'anima_animico': 'Paixão',
        'sombra': 'Entrega Excessiva',
        'personalidade': 'Equilíbrio',
        'diagnostico': 'Quando você utiliza o Vermelho Real em suas telas, traz uma energia apaixonada e intensa à sua expressão artística. Sua mensagem é de encontrar equilíbrio entre a paixão criativa e a capacidade de manter-se centrado e em controle.'
    },
    '34': {
        'cor': 'Magenta Radiante',
        'rgb': (255, 0, 144),
        'anima_animico': 'Vitalidade',
        'sombra': 'Desmantelamento',
        'personalidade': 'Integração',
        'diagnostico': 'Ao pintar com Magenta Radiante, você traz uma vitalidade e energia intensa à sua arte. Essa cor carrega a mensagem de integração, convidando-o a unificar diferentes aspectos de si mesmo e de sua expressão artística para criar uma obra coesa e significativa.'
    },
    '35': {
        'cor': 'Índigo Intenso',
        'rgb': (75, 0, 130),
        'anima_animico': 'Intuição',
        'sombra': 'Ilusões',
        'personalidade': 'Pragmatismo',
        'diagnostico': 'Ao utilizar o Índigo Intenso em suas telas, você evoca uma conexão profunda com sua intuição e sabedoria interior. Essa cor transmite a mensagem de pragmatismo, incentivando-o a abordar sua arte de forma prática e fundamentada.'
    },
    '36': {
        'cor': 'Verde Pastel',
        'rgb': (0, 128, 0),
        'anima_animico': 'Inspiração',
        'sombra': 'Imobilidade',
        'personalidade': 'Iniciativa',
        'diagnostico': 'Quando você pinta com Verde Pastel, traz uma energia inspiradora e revigorante à sua arte. Essa cor transmite a mensagem de iniciativa, convidando-o a agir e manifestar sua criatividade de forma ativa, superando qualquer sensação de imobilidade.'
    },
    '37': {
        'cor': 'Azul Sereno',
        'rgb': (0, 191, 255),
        'anima_animico': 'Paz',
        'sombra': 'Desconexão',
        'personalidade': 'Harmonia',
        'diagnostico': 'Ao utilizar o Azul Sereno em suas telas, você evoca uma sensação de paz e tranquilidade em sua expressão artística. Essa cor carrega a mensagem de harmonia, convidando-o a se conectar consigo mesmo e com o mundo ao seu redor por meio de sua arte.'
    },
    '38': {
        'cor': 'Amarelo Dourado',
        'rgb': (255, 215, 0),
        'anima_animico': 'Iluminação',
        'sombra': 'Egocentrismo',
        'personalidade': 'Generosidade',
        'diagnostico': 'Quando você pinta com Amarelo Dourado, traz uma energia de iluminação e expansão à sua arte. Essa cor transmite a mensagem de generosidade, incentivando-o a compartilhar sua criatividade e a inspirar os outros com sua expressão artística.'
    },
    '39': {
        'cor': 'Lilás Sutil',
        'rgb': (200, 162, 200),
        'anima_animico': 'Sensibilidade',
        'sombra': 'Vulnerabilidade',
        'personalidade': 'Autenticidade',
        'diagnostico': 'Ao pintar com Lilás Sutil, você evoca uma sensibilidade e delicadeza em sua arte. Essa cor carrega a mensagem de autenticidade, convidando-o a se expressar com verdade e vulnerabilidade, criando obras que tocam o coração dos espectadores.'
    },
    '40': {
        'cor': 'Marrom Quente',
        'rgb': (139, 69, 19),
        'anima_animico': 'Conexão',
        'sombra': 'Isolamento',
        'personalidade': 'Comunidade',
        'diagnostico': 'Ao utilizar o Marrom Quente em suas telas, você traz uma sensação de conexão e pertencimento à sua expressão artística. Essa cor carrega a mensagem de comunidade, incentivando-o a compartilhar sua arte e a se conectar com outros artistas e apreciadores da arte.'
    },
    '41': {
        'cor': 'Roxo Profundo',
        'rgb': (128, 0, 128),
        'anima_animico': 'Transcendência',
        'sombra': 'Obstinação',
        'personalidade': 'Flexibilidade',
        'diagnostico': 'Ao pintar com Roxo Profundo, você evoca uma sensação de transcendência e espiritualidade em sua arte. Essa cor transmite a mensagem de flexibilidade, incentivando-o a se adaptar às mudanças e explorar diferentes perspectivas em sua expressão artística.'
    },
    '42': {
        'cor': 'Ciano Vivo',
        'rgb': (0, 255, 255),
        'anima_animico': 'Expansão',
        'sombra': 'Desfoque',
        'personalidade': 'Foco',
        'diagnostico': 'Ao utilizar o Ciano Vivo em suas telas, você traz uma energia de expansão e liberdade à sua expressão artística. Essa cor carrega a mensagem de foco, convidando-o a manter a clareza e direção em sua arte, evitando distrações e desfoque.'
    },
    '43': {
        'cor': 'Amarelo Esmeralda',
        'rgb': (154, 205, 50),
        'anima_animico': 'Crescimento',
        'sombra': 'Inconstância',
        'personalidade': 'Persistência',
        'diagnostico': 'Quando você pinta com Amarelo Esmeralda, traz uma energia de crescimento e renovação à sua arte. Essa cor transmite a mensagem de persistência, incentivando-o a continuar desenvolvendo e aprimorando suas habilidades artísticas.'
    },
    '44': {
        'cor': 'Laranja Brilhante',
        'rgb': (255, 165, 0),
        'anima_animico': 'Entusiasmo',
        'sombra': 'Impaciência',
        'personalidade': 'Equilíbrio',
        'diagnostico': 'A cor Laranja Brilhante em seu processo de pintura representa entusiasmo e criatividade vibrantes. Ela convida você a abraçar sua criança interior e expressar-se com alegria e sabedoria, buscando o equilíbrio em suas emoções e ações artísticas.'
    },
    '45': {
        'cor': 'Verde Esmeralda',
        'rgb': (0, 201, 87),
        'anima_animico': 'Harmonia',
        'sombra': 'Indecisão',
        'personalidade': 'Resolução',
        'diagnostico': 'Ao pintar com Verde Esmeralda, você traz uma sensação de harmonia e equilíbrio à sua expressão artística. Essa cor carrega a mensagem de resolução, convidando-o a tomar decisões firmes e a se comprometer com sua visão artística.'
    },
    '46': {
        'cor': 'Turquesa Brilhante',
        'rgb': (64, 224, 208),
        'anima_animico': 'Energia',
        'sombra': 'Impaciência',
        'personalidade': 'Paciência',
        'diagnostico': 'Ao pintar com Turquesa Brilhante, você traz uma energia vibrante e estimulante à sua tela. Essa cor transmite uma mensagem de equilíbrio entre a energia criativa e a paciência necessária para desenvolver sua expressão artística de forma completa e satisfatória.'
    },
    '47': {
        'cor': 'Rosa Encantador',
        'rgb': (255, 105, 180),
        'anima_animico': 'Amor',
        'sombra': 'Insegurança',
        'personalidade': 'Autoaceitação',
        'diagnostico': 'Ao utilizar o Rosa Encantador em suas telas, você evoca uma energia de amor e compaixão em sua expressão artística. Essa cor carrega a mensagem de autoaceitação, convidando-o a amar e valorizar sua própria arte, superando qualquer insegurança.'
    },
    '48': {
        'cor': 'Azul Celeste',
        'rgb': (135, 206, 250),
        'anima_animico': 'Leveza',
        'sombra': 'Inconstância',
        'personalidade': 'Estabilidade',
        'diagnostico': 'A cor Azul Celeste em sua pintura representa uma sensação de leveza e tranquilidade. Sua mensagem é de estabilidade emocional, convidando-o a encontrar equilíbrio e constância em seu processo artístico, mesmo diante das mudanças e desafios.'
    },
    '49': {
        'cor': 'Dourado Radiante',
        'rgb': (255, 223, 0),
        'anima_animico': 'Prosperidade',
        'sombra': 'Ganância',
        'personalidade': 'Gratidão',
        'diagnostico': 'Ao pintar com Dourado Radiante, você evoca uma energia de prosperidade e abundância em sua arte. Essa cor carrega a mensagem de gratidão, convidando-o a valorizar e apreciar todas as conquistas e oportunidades que a arte proporciona.'
    },
    '50': {
        'cor': 'Vermelho Ardente',
        'rgb': (255, 0, 0),
        'anima_animico': 'Paixão',
        'sombra': 'Impulsividade',
        'personalidade': 'Equilíbrio',
        'diagnostico': 'Quando você utiliza o Vermelho Ardente em suas telas, traz uma energia apaixonada e intensa à sua expressão artística. Sua mensagem é de encontrar equilíbrio entre a paixão criativa e a capacidade de manter-se centrado e em controle.'
    }
}

    
# Configurações do aplicativo Streamlit
st.image("clube.png")  # Adiciona a imagem no topo do app
st.title("Análise de Cor Dominante das Pinturas de Telas")
st.write("""
Este aplicativo é uma ferramenta extremamente valiosa para o clube de artes plásticas e seus alunos. Através da análise de cor dominante em pinturas, os estudantes podem aprofundar seu entendimento sobre a influência das cores na expressão artística e como elas podem ser usadas para transmitir emoções e mensagens específicas. Além disso, a correspondência das cores com o dicionário de cores junguianas permite uma exploração mais profunda dos aspectos psicológicos das cores na arte.

A pintura em tela é uma forma de arte que permite uma grande variedade de técnicas e expressões criativas. Cada escolha de cor tem um significado e uma intenção por trás, e entender isso pode ajudar os artistas a criar obras mais expressivas e significativas. Ao usar este aplicativo, os alunos podem analisar suas próprias pinturas e entender melhor como suas escolhas de cores podem influenciar a interpretação e a recepção de suas obras.

Além disso, este aplicativo pode ser uma ferramenta educacional útil. Os professores podem usá-lo para ensinar os alunos sobre a teoria das cores e a psicologia das cores na arte. Ele pode ser usado para demonstrar em tempo real como diferentes cores podem alterar a percepção de uma pintura e como as cores podem ser usadas para transmitir diferentes emoções e significados.

Em resumo, este aplicativo pode enriquecer o processo de aprendizagem dos alunos, permitindo que eles explorem a complexa relação entre cores e emoções na arte de pintar. Também pode ser uma valiosa ferramenta de auto-reflexão, permitindo que os artistas entendam melhor suas próprias escolhas criativas e como elas afetam o impacto de suas obras.
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
    kmeans = KMeans(n_clusters=5)
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


    # Variáveis do usuário
    tema = st.text_input("Tema da Pintura")
    nome_obra = st.text_input("Nome da Obra")
    tecnica = st.text_input("Técnica Utilizada")
    dimensoes = st.text_input("Dimensões da Tela")
    idade = st.number_input("Idade do Artista", min_value=0, max_value=100)
    artista_referencia = st.text_input("Artista de Referência")
    estilo_artistico = st.text_input("Estilo Artístico")
    elemento_retratado = st.text_input("Elemento Retratado")
    descricao_figura = st.text_input("Descrição da Figura")
    genero_figura = st.text_input("Gênero da Figura")
    descricao_ambiente = st.text_input("Descrição do Ambiente")
    cor_dominante = cor_proxima["cor"]
    descricao_tecnicas = st.text_input("Descrição das Técnicas Utilizadas")
    arquetipo_junguiano = cor_proxima["anima_animico"]
    sombra = cor_proxima["sombra"]
    local_sombra = st.text_input("Local da Sombra")
    interpretacao_sombra = st.text_input("Interpretação da Sombra")
    cor_correspondente_sombra = cor_proxima["cor"]
    local_personalidade = st.text_input("Local da Personalidade")
    interpretacao_personalidade = st.text_input("Interpretação da Personalidade")
    contexto_relevante = st.text_input("Contexto Relevante")

    # Definição do template
    texto_template = """
    Tema: {tema}
    
    Nome da Obra: {nome_obra}
    
    Técnica Utilizada: {tecnica}
    
    Dimensões da Tela: {dimensoes}
    
    Idade do Artista: {idade}
    
    Artista de Referência: {artista_referencia}
    
    Estilo Artístico: {estilo_artistico}

    Elemento Retratado: {elemento_retratado}
    
    Descrição da Figura: {descricao_figura}
    
    Gênero da Figura: {genero_figura}

    Descrição do Ambiente: {descricao_ambiente}
    
    Cor Dominante: {cor_dominante}

    Descrição das Técnicas Utilizadas: {descricao_tecnicas}

    Arquétipo Junguiano: {arquetipo_junguiano}

    Sombra: {sombra}
    
    Local da Sombra: {local_sombra}
    
    Interpretação da Sombra: {interpretacao_sombra}
    
    Cor Correspondente à Sombra: {cor_correspondente_sombra}

    Local da Personalidade: {local_personalidade}
    
    Interpretação da Personalidade: {interpretacao_personalidade}
    
    Contexto Relevante: {contexto_relevante}
    """

    # Preenchendo o template com as variáveis do usuário
    texto_final = texto_template.format(
        tema=tema,
        nome_obra=nome_obra,
        tecnica=tecnica,
        dimensoes=dimensoes,
        idade=idade,
        artista_referencia=artista_referencia,
        estilo_artistico=estilo_artistico,
        elemento_retratado=elemento_retratado,
        descricao_figura=descricao_figura,
        genero_figura=genero_figura,
        descricao_ambiente=descricao_ambiente,
        cor_dominante=cor_dominante,
        descricao_tecnicas=descricao_tecnicas,
        arquetipo_junguiano=arquetipo_junguiano,
        sombra=sombra,
        local_sombra=local_sombra,
        interpretacao_sombra=interpretacao_sombra,
        cor_correspondente_sombra=cor_correspondente_sombra,
        local_personalidade=local_personalidade,
        interpretacao_personalidade=interpretacao_personalidade,
        contexto_relevante=contexto_relevante
    )

    # Exibindo o texto final
    st.subheader("Texto Final")
    st.write(texto_final)




