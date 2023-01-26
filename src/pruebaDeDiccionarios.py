def main():
    # Declarando el diccionario
    alumno = {"Nombre": "Julian", "Apellido": "Ruiz Diaz"}

    # Imprimiendo el diccionario
    print(alumno)

    # Alta
    alumno["Padron"] = 108411
    print(alumno)

    # Modificacion
    alumno["Padron"] = 108410
    print(alumno)

    # Baja
    del alumno["Padron"]
    print(alumno)

    # Iterando
    for llave, valor in alumno.items():
        print(f"{llave}: {valor}")

    # Comparando
    otroAlumno = {"Apellido": "Ruiz Diaz", "Nombre": "Julian"}
    print(alumno == otroAlumno)

    # Copia (TENER MUCHO CUIDADO)
    otroAlumno = alumno
    alumno["Padron"] = 108415
    print(otroAlumno)
    print(alumno)


main()
