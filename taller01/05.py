import cv2
import matplotlib.pyplot as plt

def mi_escala_grises(img_rgb):
    """
    Convierte una imagen RGB a escala de grises.

    Proceso:
        - Separa los canales R, G y B.
        - Aplica una combinacion ponderada para aproximar la luminancia.

    Parametros:
        - img_rgb: imagen de entrada con tres canales (altura x ancho x 3).

    Retorna:
        - Imagen en escala de grises (uint8) con un solo canal.
    """
    R = img_rgb[:, :, 0]
    G = img_rgb[:, :, 1]
    B = img_rgb[:, :, 2]

    # Ponderacion clasica de luminancia para cada canal
    gray = 0.299 * R + 0.587 * G + 0.114 * B
    return gray.astype('uint8')
img = mi_escala_grises(cv2.imread('images/color.jpeg'))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Mostrar la imagen utilizando matplotlib (para trabajar con RGB)
plt.imshow(img_rgb)
plt.axis('off')  # Ocultar los ejes
plt.show()