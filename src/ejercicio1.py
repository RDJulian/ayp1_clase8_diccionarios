NOMBRE = "NOMBRE"
APELLIDO = "APELLIDO"
PADRON = "PADRON"


def crear_alumno() -> dict:
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    padron = int(input("Ingrese padrón: "))
    alumno = {NOMBRE: nombre, APELLIDO: apellido, PADRON: padron}
    return alumno


def buscar_alumno(alumnos: list) -> int:
    nombre = input("Ingrese un nombre a buscar: ")
    indice = -1
    i = 0
    while i < len(alumnos) and indice == -1:
        if alumnos[i][NOMBRE] == nombre:
            indice = i
        else:
            i += 1
    return indice


def imprimir_alumnos(alumnos):
    for alumno in alumnos:
        print(f"Nombre -> {alumno[NOMBRE]}")
        print(f"Apellido -> {alumno[APELLIDO]}")
        print(f"Padron -> {alumno[PADRON]}")
        print()


def main():
    alumnos = []
    opcion = "0"
    while opcion != "4":
        print("1. Alta\n2. Consulta\n3. Listar\n4. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            alumno = crear_alumno()
            alumnos.append(alumno)
        elif opcion == "2":
            indice = buscar_alumno(alumnos)
            if indice != -1:
                print(alumnos[indice])
            else:
                print("El alumno no fue encontrado.")
        elif opcion == "3":
            imprimir_alumnos(alumnos)
        elif opcion != "4":
            print("Opcion incorrecta.")


if __name__ == "__main__":
    main()
