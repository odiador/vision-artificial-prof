# Codficación python
import cv2
import matplotlib.pyplot as plt

# Leer la imagen (en formato RGB)
img = cv2.imread('images/color.jpeg')

# Convertir la imagen de BGR a RGB (OpenCV usa BGR por defecto)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Mostrar la imagen utilizando matplotlib (para trabajar con RGB)
plt.imshow(img_rgb)
plt.axis('off')  # Ocultar los ejes
plt.show()

# Guardar la imagen en un nuevo archivo
cv2.imwrite('imagen_guardada.jpg', img)
