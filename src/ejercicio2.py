from lectura_archivo import cargar_datos, guardar_datos


def crear_modelo(modelos: dict) -> None:
    nombre = input("Ingrese Nombre del modelo: ")
    if nombre in modelos.keys():
        print("Ya existe ese modelo.")
    else:
        stock = int(input("Ingrese Stock: "))
        precio = int(input("Ingrese Precio: "))
        informacion_modelo = {"Stock": {"XS": stock,
                                        "S": stock,
                                        "M": stock,
                                        "L": stock,
                                        "XL": stock},
                              "Precio": precio}
        modelos[nombre] = informacion_modelo


def cargar_modelos() -> dict:
    datos = cargar_datos("modelos")
    modelos = {}
    if datos:
        modelos = datos
    return modelos


def main():
    modelos = cargar_modelos()
    opcion = "0"
    while opcion != "7":
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            crear_modelo(modelos)
        elif opcion == "2":
            # Completar
            pass
    guardar_datos(modelos, "modelos")


if __name__ == "__main__":
    main()
