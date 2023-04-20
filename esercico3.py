import cv2

# carregar a imagem
image = cv2.imread('imagem.jpg')

# aplicar filtro de borramento
blur = cv2.GaussianBlur(image, (5,5), 0)

# exibir a imagem original e a filtrada
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Filtrada', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()