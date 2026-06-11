inventario = {
    "Laptop": 10,
    "Mouse": 25,
    "Teclado": 15
}

print("Inventario")
for producto in inventario:
    print(producto,"->",inventario[producto],"unidades")

nombre_producto = input("Ingrese nombre producto: ").strip().title()

if not nombre_producto:
    print("El nombre del producto no puede estar vacío")
else:
    if nombre_producto not in inventario:
        print("El producto no existe en el inventario")
    else:
        cantidad_ingresada = input("Ingrese cantidad a vender: ")
        try:
            cantidad = int(cantidad_ingresada)
        except ValueError:
            print("La cantidad debe ser un número entero")
        else:
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero")
            elif cantidad <= inventario[nombre_producto]:
                print("\nVenta realizada")
                inventario[nombre_producto] -= cantidad
                print(f"{nombre_producto}: {inventario[nombre_producto]} unidades")
            else:
                print("No existe stock suficiente!")
