from os import path
from pickle import load, dump
from typing import Any

"""
Este archivo utiliza la librería 'pickle' para guardar los datos
en un archivo, solamente para no tener que cargar constantemente los datos
en distintas ejecuciones del programa.
Lo pueden ignorar si quieren, pero recomiendo buscar la documentación.
"""


def cargar_datos(ruta: str) -> Any | None:
    """
    PRE:
    POST: Devuelve los datos si el archivo existe, None de lo contrario.
    """
    if path.isfile(ruta):
        with open(ruta, "rb") as archivo:
            datos = load(archivo)
        return datos
    else:
        return None


def guardar_datos(datos: Any, ruta: str) -> None:
    """
    PRE:
    POST: Guarda los datos en un archivo binario.
    """
    with open(ruta, "wb") as archivo:
        dump(datos, archivo)
