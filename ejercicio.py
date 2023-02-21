# Diccionarios
productos = {1: "Pantalones", 2: "Camisas", 3: "Corbatas", 4: "Casacas"}
precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
stock = {1: 50, 2: 45, 3: 30, 4: 15}

# Función para mostrar la tabla productos
def mostrar_tabla_productos():
    print("====================================================")
    print("Lista de Productos:")
    print("====================================================")
    print("ID \t Producto \t Precio \t Stock")
    print("====================================================")
    for id_producto, producto in productos.items():
        print(f"{id_producto} \t {producto} \t {precios[id_producto]} \t\t {stock[id_producto]}")
    print("====================================================")

# Función para agregar producto
def agregar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    if id_producto in productos:
        print("El producto ya existe.")
    else:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad en stock del producto: "))
        productos[id_producto] = nombre
        precios[id_producto] = precio
        stock[id_producto] = cantidad
        print("Producto agregado correctamente.")

# Función para eliminar producto
def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    if id_producto not in productos:
        print("El producto no existe en la lista.")
    else:
        del productos[id_producto]
        del precios[id_producto]
        del stock[id_producto]
        print("Producto eliminado correctamente.")

# Función para actualizar producto
def actualizar_producto():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    if id_producto not in productos:
        print("El producto no existe.")
    else:
        nombre = input("Ingrese el nuevo nombre del producto: ")
        precio = float(input("Ingrese el nuevo precio del producto: "))
        new_stock = int(input("Ingrese el nuevo stock del producto: "))
        productos[id_producto] = nombre
        precios[id_producto] = precio
        stock[id_producto] = new_stock
        print("Producto actualizado correctamente.")

# Mostramos la tabla de productos por primera vez
mostrar_tabla_productos()

# Menú de opciones
while True:
    # Mostramos las opciones
    print("Seleccione una opción:")
    print("[1] Agregar")
    print("[2] Eliminar")
    print("[3] Actualizar")
    print("[4] Salir")
    opcion = input()

    # Ejecutamos la opción seleccionada
    if opcion == "1":
        agregar_producto()
        mostrar_tabla_productos()
    elif opcion == "2":
        eliminar_producto()
        mostrar_tabla_productos()
    elif opcion == "3":
        actualizar_producto()
        mostrar_tabla_productos()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")