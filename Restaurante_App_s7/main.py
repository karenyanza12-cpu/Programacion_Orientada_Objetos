from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear el servicio principal
restaurante = Restaurante()


# Menú principal
while True:

    print("\n========================================")
    print("       SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")

    opcion = input("\nSeleccione una opción: ")

    # Registrar producto
    if opcion == "1":

        print("\nREGISTRAR PRODUCTO")

        nombre = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))

        respuesta = input("¿Está disponible? (S/N): ").upper()

        if respuesta == "S":
            disponible = True
        else:
            disponible = False

        producto = Producto(
            nombre,
            categoria,
            precio,
            disponible
        )

        restaurante.registrar_producto(producto)

    # Listar productos
    elif opcion == "2":

        restaurante.listar_productos()

    # Buscar producto
    elif opcion == "3":

        nombre = input("Ingrese el nombre del producto: ")

        restaurante.buscar_producto(nombre)

    # Registrar cliente
    elif opcion == "4":

        print("\nREGISTRAR CLIENTE")

        id_cliente = int(input("ID del cliente: "))
        nombre = input("Nombre: ")
        correo = input("Correo electrónico: ")

        cliente = Cliente(
            id_cliente,
            nombre,
            correo
        )

        restaurante.registrar_cliente(cliente)

    # Listar clientes
    elif opcion == "5":

        restaurante.listar_clientes()

    # Buscar cliente
    elif opcion == "6":

        nombre = input("Ingrese el nombre del cliente: ")

        restaurante.buscar_cliente(nombre)

    # Salir
    elif opcion == "7":

        print("\nGracias por utilizar el sistema.")
        break

    else:

        print("\nOpción no válida.")
        