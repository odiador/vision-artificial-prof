import os
import cv2


def cargar_variantes(ruta_imagen):
    """
    Lee una imagen y genera tres variantes: gris, binaria y color (BGR).

    Proceso:
        - Lee la imagen en escala de grises.
        - Aplica un umbral fijo para obtener la binaria.
        - Lee la imagen a color (BGR).

    Parametros:
        - ruta_imagen: ruta del archivo de imagen a cargar.

    Retorna:
        - Tuple con (img_gray, img_binary, img_bgr).
    """
    img_gray = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    _, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    img_bgr = cv2.imread(ruta_imagen)
    return img_gray, img_binary, img_bgr


def guardar_variantes(base_dir, nombre_base, variantes, formatos):
    """
    Guarda las variantes de una imagen en multiples formatos.

    Proceso:
        - Crea los nombres de archivo por variante y formato.
        - Guarda cada imagen en el formato solicitado.

    Parametros:
        - base_dir: carpeta destino.
        - nombre_base: nombre base para los archivos (sin extension).
        - variantes: dict con claves {'gray','binary','bgr'} y sus imagenes.
        - formatos: lista de extensiones, por ejemplo ['bmp','png','jpg'].
    """
    for formato in formatos:
        cv2.imwrite(
            os.path.join(base_dir, f"{nombre_base}_gray.{formato}"),
            variantes["gray"],
        )
        cv2.imwrite(
            os.path.join(base_dir, f"{nombre_base}_binary.{formato}"),
            variantes["binary"],
        )
        cv2.imwrite(
            os.path.join(base_dir, f"{nombre_base}_rgb.{formato}"),
            variantes["bgr"],
        )


def main():
    formatos = ["bmp", "png", "jpg"]
    imagenes = {
        "dark": "images/dark.png",
        "some": "images/some.png",
        "color": "images/color.jpeg",
    }

    for nombre, ruta in imagenes.items():
        img_gray, img_binary, img_bgr = cargar_variantes(ruta)
        variantes = {"gray": img_gray, "binary": img_binary, "bgr": img_bgr}
        destino = os.path.join("formats", nombre)
        guardar_variantes(destino, nombre, variantes, formatos)


if __name__ == "__main__":
    main()
