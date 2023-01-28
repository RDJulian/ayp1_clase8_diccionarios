from os import path
from pickle import dump, load


# Pickle: ignorar
def cargarDatos() -> list:
    """
    PRE:
    POST: Devuelve la lista si habia un archivo guardado o una vacia de lo contrario.
    """
    if path.isfile("alumnos"):
        with open("alumnos", "rb") as archivo:
            alumnos = load(archivo)
        return alumnos
    else:
        return []


def guardarDatos(alumnos: list) -> None:
    """
    PRE:
    POST: Guarda la lista (vacia o no) en un archivo binario.
    """
    with open("alumnos", "wb") as archivo:
        dump(alumnos, archivo)


# Solucion
def agregarAlumno(alumnos: list) -> None:
    """
    PRE:
    POST: Se agrega un nuevo alumno a la lista, con un Padron (int), Nombre (str) y Apellido (str).
    """
    padron = int(input("Ingrese el padron: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    alumno = {"Padron": padron, "Nombre": nombre, "Apellido": apellido}
    alumnos.append(alumno)


def buscarAlumno(alumnos: list) -> dict | None:
    """
    PRE: Los alumnos que esten en la lista deben tener una llave "Nombre".
    POST: Devuelve el alumno buscado si coincide el nombre ingresado, None en caso contrario.
    """
    nombre = input("Ingrese el nombre a buscar: ")
    indice = 0
    alumnoBuscado = None
    while indice < len(alumnos) and alumnoBuscado is None:
        if alumnos[indice]["Nombre"] == nombre:
            alumnoBuscado = alumnos[indice]
        indice += 1
    return alumnoBuscado


def imprimirAlumno(alumno: dict | None) -> None:
    """
    PRE: El alumno debe tener las tres llaves ("Nombre", "Apellido", "Padron"), en caso de no ser None.
    POST: Se imprime la información del alumno, o un mensaje de error si se recibe None.
    """
    if alumno is not None:
        print(f'Padron: {alumno["Padron"]}\nNombre: {alumno["Nombre"]}\nApellido: {alumno["Apellido"]}\n')
    else:
        print("El alumno no fue encontrado.\n")


def imprimirAlumnos(alumnos: list) -> None:
    """
    PRE: Todos alumnos deben tener las tres llaves ("Nombre", "Apellido", "Padron").
    POST: Se imprime la información de todos los alumnos en la lista.
    """
    for alumno in alumnos:
        imprimirAlumno(alumno)


def imprimirMenu() -> None:
    """
    PRE:
    POST: Se imprime el menu de opciones válidas.
    """
    print(
        f"1. Agregar alumno\n2. Buscar alumno por nombre\n3. Imprimir la informacion de todos los alumnos\n4. Salir\n")


def main() -> None:
    alumnos = cargarDatos()
    opcion = 0
    while not opcion == 4:
        imprimirMenu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregarAlumno(alumnos)
        elif opcion == 2:
            alumno = buscarAlumno(alumnos)
            imprimirAlumno(alumno)
        elif opcion == 3:
            imprimirAlumnos(alumnos)
    guardarDatos(alumnos)


main()
