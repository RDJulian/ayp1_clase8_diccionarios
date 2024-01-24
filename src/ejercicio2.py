from lectura_archivo import guardar_datos, cargar_datos

"""
Nota: esta solución está deliberadamente incompleta.
Se escribio en muy poco tiempo en la clase del año 2023.
Dejo comentarios con casos borde para pensar y validar.
Se puede mejorar muchisimo este programa...
"""


def agregar_modelo(camisetas: dict) -> None:
    """
    PRE:
    POST: Agrega un nuevo modelo.
    """
    nombre = input("Ingrese el nombre del modelo: ")
    # ¿Stock negativo?
    stock = int(input("Ingrese el stock inicial: "))
    # ¿Precio negativo?
    precio = int(input("Ingrese el precio: "))
    # ¿Qué pasa si ya existe el modelo?
    camisetas[nombre] = {"XS": stock, "S": stock, "M": stock, "L": stock, "XL": stock, "Precio": precio}


def eliminar_modelo(camisetas: dict) -> None:
    """
    PRE:
    POST: Elimina el modelo elegido.
    """
    nombre = input("Ingrese el nombre del modelo: ")
    # ¿Qué pasa si no existe el modelo?
    del camisetas[nombre]


def comprar_camisetas(camisetas: dict) -> int:
    """
    PRE:
    POST: Compra camisetas del modelo y talle elegido (efectivamente bajando el stock).
    """
    nombre = input("Ingrese el nombre del modelo: ")
    # ¿Talle incorrecto?
    talle = input("Ingrese el talle: ")
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    # ¿Qué pasa si hay menos stock del que se quiere comprar?
    # ¿Cantidad negativa?
    camisetas[nombre][talle] -= cantidad
    return camisetas[nombre]["Precio"] * cantidad


def agregar_stock(camisetas: dict) -> None:
    """
    PRE:
    POST: Agrega stock al modelo elegido.
    """
    # ¿Qué pasa si no existe el modelo?
    nombre = input("Ingrese el nombre del modelo: ")
    # ¿Tiene sentido un stock negativo?
    stock = int(input("Ingrese el stock a agregar: "))
    # ¿Se puede mejorar?
    camisetas[nombre]["XS"] += stock
    camisetas[nombre]["S"] += stock
    camisetas[nombre]["M"] += stock
    camisetas[nombre]["L"] += stock
    camisetas[nombre]["XL"] += stock


def cambiar_precio(camisetas: dict) -> None:
    """
    PRE:
    POST: Cambia el precio del modelo elegido.
    """
    nombre = input("Ingrese el nombre del modelo: ")
    precio = int(input("Ingrese el precio: "))
    # ¿Modelo incorrecto, precio negativo?
    camisetas[nombre]["Precio"] = precio


def calcular_valor_modelo(camisetas: dict, modelo: str) -> int:
    """
    PRE:
    POST: Calcula y devuelve el valor total del modelo.
    """
    stock_total = 0
    # ¿Se puede mejorar?
    stock_total += camisetas[modelo]["XS"]
    stock_total += camisetas[modelo]["S"]
    stock_total += camisetas[modelo]["M"]
    stock_total += camisetas[modelo]["L"]
    stock_total += camisetas[modelo]["XL"]
    return stock_total * camisetas[modelo]["Precio"]


def mostrar_recaudacion(recaudacion: int) -> None:
    """
    PRE:
    POST: Imprime la recaudación total.
    """
    print(f"La recaudacion total es de: {recaudacion} pesos.")


def imprimir_valor_modelo(nombre: str, valor: int) -> None:
    """
    PRE:
    POST: Imprime el valor total del modelo.
    """
    print(f"El valor total del modelo {nombre} es de: {valor} pesos.")


def imprimir_opciones() -> None:
    """
    PRE:
    POST: Imprime el menu de opciones válidas.
    """
    print(
        f"1. Dar de alta un modelo\n2. Dar de baja un modelo\n3. Comprar camiseta\n4. Agregar stock\n5. Cambiar "
        f"precio\n6. Mostrar valor de un modelo\n7. Mostrar recaudacion\n8. Salir\n")


def main():
    datos = cargar_datos("camisetas")
    if datos:
        camisetas, recaudacion = datos
    else:
        camisetas = {}
        recaudacion = 0
    opcion = 0
    while not opcion == 8:
        imprimir_opciones()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_modelo(camisetas)
        elif opcion == 2:
            eliminar_modelo(camisetas)
        elif opcion == 3:
            recaudacion += comprar_camisetas(camisetas)
        elif opcion == 4:
            agregar_stock(camisetas)
        elif opcion == 5:
            cambiar_precio(camisetas)
        elif opcion == 6:
            nombre = input("Ingrese el nombre del modelo: ")
            valor = calcular_valor_modelo(camisetas, nombre)
            imprimir_valor_modelo(nombre, valor)
        elif opcion == 7:
            mostrar_recaudacion(recaudacion)
    guardar_datos((camisetas, recaudacion), "camisetas")


if __name__ == "__main__":
    main()
