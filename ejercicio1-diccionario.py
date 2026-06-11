agenda = {}

for x in range(3):
    nombre = input("Ingrese nombre: ").strip().title()
    if not nombre:
        print("El nombre no puede estar vacío")
        break
    telefono_ingresado = input("Ingrese teléfono: ")
    try:
        telefono = int(telefono_ingresado)
    except ValueError:
        print("El teléfono debe ser un número entero")
        break
    agenda[nombre] = telefono

print("Agenda:")
for clave in agenda:
    print(clave,"->",agenda[clave])

agenda = []

for x in range(3):
    nombre = input("Ingrese nombre: ").strip().title()
    if not nombre:
        print("El nombre no puede estar vacío")
        break
    telefono_ingresado = input("Ingrese teléfono: ")
    try:
        telefono = int(telefono_ingresado)
    except ValueError:
        print("El teléfono debe ser un número entero")
        break
    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }
    agenda.append(contacto)

for contacto in agenda:
    print( contacto["nombre"],"->",contacto["telefono"] )
