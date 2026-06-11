notas = {
    "Pedro": 5.5,
    "María": 6.2,
    "Juan": 4.8,
    "Ana": 7.0
}

nombre = input("Ingrese nombre: ").strip().title()

if not nombre:
    print("El nombre no puede estar vacío")
else:
    if notas.get(nombre):
        print(f"La nota de {nombre} es {notas[nombre]}")
        if notas[nombre] >= 4:
            print("Aprobado")
        else:
            print("Reprobado")
    else:
        print("Alumno no encontrado")

    try:
        print(f"La nota de {nombre} es {notas[nombre]}")
        if notas[nombre] >= 4:
            print("Aprobado")
        else:
            print("Reprobado")
    except:
        print("Alumno no encontrado")

    if nombre in notas:
        print(f"La nota de {nombre} es {notas[nombre]}")
        if notas[nombre] >= 4:
            print("Aprobado")
        else:
            print("Reprobado")
    else:
        print("Alumno no encontrado")
