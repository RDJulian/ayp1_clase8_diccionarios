def main():
    # Instanciando el diccionario de forma explicita.
    alumno = {"Nombre": "Julian", "Apellido": "Ruiz Diaz"}

    # Imprimiendo el diccionario
    print(alumno, end="\n\n")

    # Alta
    alumno["Padron"] = 108411
    print(alumno, end="\n\n")

    # Consulta / Acceso
    print(alumno["Padron"], end="\n\n")

    # Modificación
    alumno["Padron"] = 108410
    # La clave "Padron" ya existía.
    print(alumno, end="\n\n")

    # Baja
    del alumno["Padron"]
    print(alumno, end="\n\n")

    # Comparación
    alumno2 = {"Apellido": "Ruiz Diaz", "Nombre": "Julian"}
    print(alumno == alumno2, end="\n\n")

    # ¿Copia? (TENER MUCHO CUIDADO)
    alumno2 = alumno
    alumno["Padron"] = 108415
    print(alumno)
    print(alumno2, end="\n\n")

    # Copia
    alumno2 = alumno.copy()
    alumno["Padron"] = 109000
    print(alumno)
    print(alumno2, end="\n\n")

    # Demostración de las distintas iteraciones posibles:
    for clave in alumno.keys():
        print(clave)
        print(alumno[clave])
    print()

    for valor in alumno.values():
        print(valor)
    print()

    for clave, valor in alumno.items():
        print(f"{clave} : {valor}")


if __name__ == "__main__":
    main()
