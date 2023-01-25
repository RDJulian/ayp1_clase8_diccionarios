from os import path
from pickle import dump, load


# Pickle: ignorar
def cargarDatos() -> tuple:
    """
    PRE:
    POST: Devuelve el diccionario y la recaudacion si había un archivo guardado.
    Devuelve un diccionario vacio y 0 en caso contrario.
    """
    if path.isfile("camisetas"):
        with open("camisetas", "rb") as archivo:
            camisetas, recaudacion = load(archivo)
        return camisetas, recaudacion
    else:
        return {}, 0


def guardarDatos(camisetas: dict, recaudacion: int) -> None:
    """
    PRE:
    POST: Guarda el diccionario (vacio o no) y la recaudacion en un archivo binario.
    """
    with open("camisetas", "wb") as archivo:
        dump((camisetas, recaudacion), archivo)


# Solucion
def agregarModelo(camisetas):
    nombre = input("Ingrese el nombre del modelo: ")
    stock = int(input("Ingrese el stock inicial: "))
    precio = int(input("Ingrese el precio: "))
    camisetas[nombre] = {"XS": stock, "S": stock, "M": stock, "L": stock, "XL": stock, "Precio": precio}


def eliminarModelo(camisetas):
    nombre = input("Ingrese el nombre del modelo: ")
    del camisetas[nombre]


def comprarCamisetas(camisetas):
    nombre = input("Ingrese el nombre del modelo: ")
    talle = input("Ingrese el talle: ")
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    camisetas[nombre][talle] -= cantidad
    return camisetas[nombre]["Precio"] * cantidad


def agregarStock(camisetas):
    nombre = input("Ingrese el nombre del modelo: ")
    stock = int(input("Ingrese el stock a agregar: "))
    camisetas[nombre]["XS"] += stock
    camisetas[nombre]["S"] += stock
    camisetas[nombre]["M"] += stock
    camisetas[nombre]["L"] += stock
    camisetas[nombre]["XL"] += stock


def cambiarPrecio(camisetas):
    nombre = input("Ingrese el nombre del modelo: ")
    precio = int(input("Ingrese el precio: "))
    camisetas[nombre]["Precio"] = precio


def calcularValorModelo(camisetas):
    nombre = input("Ingrese el nombre del modelo: ")
    stockTotal = 0
    stockTotal += camisetas[nombre]["XS"]
    stockTotal += camisetas[nombre]["S"]
    stockTotal += camisetas[nombre]["M"]
    stockTotal += camisetas[nombre]["L"]
    stockTotal += camisetas[nombre]["XL"]
    return nombre, stockTotal * camisetas[nombre]["Precio"]


def mostrarRecaudacion(recaudacion):
    print(f"La recaudacion total es de: {recaudacion} pesos.")


def imprimirValorModelo(nombre, valor):
    print(f"El valor total del modelo {nombre} es de: {valor} pesos.")


def imprimirMenu():
    print(
        f"1. Dar de alta un modelo\n2. Dar de baja un modelo\n3. Comprar camiseta\n4. Agregar stock\n5. Cambiar "
        f"precio\n6. Mostrar valor de un modelo\n7. Mostrar recaudacion\n8. Salir\n")


def main():
    camisetas, recaudacion = cargarDatos()
    opcion = 0
    while not opcion == 8:
        imprimirMenu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregarModelo(camisetas)
        elif opcion == 2:
            eliminarModelo(camisetas)
        elif opcion == 3:
            recaudacion += comprarCamisetas(camisetas)
        elif opcion == 4:
            agregarStock(camisetas)
        elif opcion == 5:
            cambiarPrecio(camisetas)
        elif opcion == 6:
            nombre, valor = calcularValorModelo(camisetas)
            imprimirValorModelo(nombre, valor)
        elif opcion == 7:
            mostrarRecaudacion(recaudacion)
    guardarDatos(camisetas, recaudacion)


main()
