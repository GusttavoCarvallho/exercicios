import mahotas as mh
import matplotlib.pyplot as plt

# carregar a imagem
image = mh.imread('imagem.jpg')

# mostrar a imagem
plt.imshow(image)
plt.show()
