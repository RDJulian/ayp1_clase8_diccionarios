from lectura_archivo import guardar_datos, cargar_datos


def agregar_alumno(alumnos: list) -> None:
    """
    PRE:
    POST: Agrega un nuevo alumno a la lista, con un Padron, Nombre y Apellido.
    """
    padron = int(input("Ingrese el padron: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    # Se podría chequear que no exista.
    alumno = {"Padron": padron, "Nombre": nombre, "Apellido": apellido}
    alumnos.append(alumno)


def buscar_alumno(alumnos: list) -> int:
    """
    PRE: Los alumnos que esten en la lista deben tener una llave "Nombre".
    POST: Devuelve el indice del alumno buscado si coincide el nombre ingresado,
    -1 en caso contrario.
    """
    nombre = input("Ingrese el nombre a buscar: ")
    i = 0
    indice = -1
    while i < len(alumnos) and indice == -1:
        if alumnos[i]["Nombre"] == nombre:
            indice = i
        else:
            i += 1
    return indice


def imprimir_alumno(alumno: dict) -> None:
    """
    PRE: El alumno debe tener las tres llaves ("Nombre", "Apellido", "Padron").
    POST: Imprime la información del alumno.
    """
    print(f'Padron: {alumno["Padron"]}\nNombre: {alumno["Nombre"]}\nApellido: {alumno["Apellido"]}\n')


def imprimir_alumnos(alumnos: list) -> None:
    """
    PRE: Todos alumnos deben tener las tres llaves ("Nombre", "Apellido", "Padron").
    POST: Imprime la información de todos los alumnos en la lista.
    """
    for alumno in alumnos:
        imprimir_alumno(alumno)


def imprimir_opciones() -> None:
    """
    PRE:
    POST: Imprime el menu de opciones válidas.
    """
    print(
        f"1. Agregar alumno\n2. Buscar alumno por nombre\n3. Imprimir la informacion de todos los alumnos\n4. Salir\n")


def main():
    datos = cargar_datos("alumnos")
    if datos:
        alumnos = datos
    else:
        alumnos = []
    opcion = 0
    while not opcion == 4:
        imprimir_opciones()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_alumno(alumnos)
        elif opcion == 2:
            indice = buscar_alumno(alumnos)
            if indice == -1:
                print("El alumno no fue encontrado.")
            else:
                imprimir_alumno(alumnos[indice])
        elif opcion == 3:
            imprimir_alumnos(alumnos)
    guardar_datos(alumnos, "alumnos")


if __name__ == "__main__":
    main()
