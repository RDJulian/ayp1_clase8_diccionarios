from lectura_archivo import cargar_datos, guardar_datos

ALTA_MODELO = "1"
MOSTRAR_MODELO = "2"
SALIR = "7"


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
    opcion = ""
    while opcion != SALIR:
        opcion = input("Ingrese una opcion: ")
        if opcion == ALTA_MODELO:
            crear_modelo(modelos)
        elif opcion == MOSTRAR_MODELO:
            # Completar
            pass
        elif opcion != SALIR:
            print("Opcion incorrecta.")
    guardar_datos(modelos, "modelos")


if __name__ == "__main__":
    main()
