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
    alumno2 = {"Apellido": "Ruiz Diaz", "Nombre": "Julian"}
    print(alumno == alumno2)

    # Copia (TENER MUCHO CUIDADO)
    alumno2 = alumno
    alumno["Padron"] = 108415
    print(alumno)
    print(alumno2)


if __name__ == "__main__":
    main()
