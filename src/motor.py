import os 

NOMBRE_ARCHIVO = "record.txt"

def obtener_record():
    # Lee el record desde el archivo .txt, si no existe devuelve 0
    if not os.path.exists(NOMBRE_ARCHIVO):
        return 0
    try:
        with open(NOMBRE_ARCHIVO, "r") as f:
            contenido = f.read().strip()
            return int(contenido) if contenido else 0
    except (ValueError, IOError):
        return 0


def guardar_record(puntos):
    # Compara los puntos actuales con el record y actualiza si es necesario
    actual = obtener_record()
    if puntos > actual:
        with open(NOMBRE_ARCHIVO, "w") as f:
            f.write(str(puntos))
