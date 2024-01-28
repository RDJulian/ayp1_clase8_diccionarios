from lectura_archivo import cargar_datos, guardar_datos

# Se puede discutir si estas tres constantes son necesarias.
NOMBRE = "NOMBRE"
APELLIDO = "APELLIDO"
PADRON = "PADRON"

ALTA_ALUMNO = "1"
BUSCAR_ALUMNO = "2"
LISTAR_ALUMNOS = "3"
SALIR = "4"

NO_ENCONTRADO = -1


def crear_alumno() -> dict:
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    padron = int(input("Ingrese padrón: "))
    alumno = {NOMBRE: nombre, APELLIDO: apellido, PADRON: padron}
    return alumno


def buscar_alumno(alumnos: list, nombre: str) -> int:
    indice = NO_ENCONTRADO
    i = 0
    while i < len(alumnos) and indice == NO_ENCONTRADO:
        if alumnos[i][NOMBRE] == nombre:
            indice = i
        else:
            i += 1
    return indice


def imprimir_alumnos(alumnos: list) -> None:
    for alumno in alumnos:
        print(f"Nombre -> {alumno[NOMBRE]}")
        print(f"Apellido -> {alumno[APELLIDO]}")
        print(f"Padron -> {alumno[PADRON]}")
        print()


def cargar_alumnos() -> list:
    datos = cargar_datos("alumnos")
    alumnos = []
    if datos:
        alumnos = datos
    return alumnos


def main():
    alumnos = cargar_alumnos()
    opcion = ""
    while opcion != SALIR:
        print("1. Alta\n2. Consulta\n3. Listar\n4. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == ALTA_ALUMNO:
            alumno = crear_alumno()
            alumnos.append(alumno)
        elif opcion == BUSCAR_ALUMNO:
            nombre = input("Ingrese un nombre a buscar: ")
            indice = buscar_alumno(alumnos, nombre)
            if indice != NO_ENCONTRADO:
                print(alumnos[indice])
            else:
                print("El alumno no fue encontrado.")
        elif opcion == LISTAR_ALUMNOS:
            imprimir_alumnos(alumnos)
        elif opcion != SALIR:
            print("Opcion incorrecta.")
    guardar_datos(alumnos, "alumnos")


if __name__ == "__main__":
    main()
