from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


# Crear el restaurante
restaurante = Restaurante()


def registrar_producto():
    print("\n=== REGISTRAR PRODUCTO ===")

    try:
        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))

        disponible = input("¿Está disponible? (si/no): ").lower() == "si"

        if not nombre.strip():
            print("El nombre no puede estar vacío.")
            return

        if not categoria.strip():
            print("La categoría no puede estar vacía.")
            return

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            return

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            disponible
        )

        restaurante.registrar_producto(producto)

    except ValueError:
        print("Error: ingrese datos válidos.")


def buscar_producto():
    print("\n=== BUSCAR PRODUCTO ===")

    try:
        codigo = int(input("Ingrese el código del producto: "))

        producto = restaurante.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
        else:
            producto.mostrar_informacion()

    except ValueError:
        print("El código debe ser un número entero.")


def actualizar_producto():
    print("\n=== ACTUALIZAR PRODUCTO ===")

    try:
        codigo = int(input("Ingrese el código del producto: "))

        producto = restaurante.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return

        print("\nIngrese los nuevos datos:")

        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        precio = float(input("Nuevo precio: "))
        disponible = input("¿Está disponible? (si/no): ").lower() == "si"

        if not nombre.strip():
            print("El nombre no puede estar vacío.")
            return

        if not categoria.strip():
            print("La categoría no puede estar vacía.")
            return

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            return

        restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            disponible
        )

    except ValueError:
        print("Error: ingrese datos válidos.")


def eliminar_producto():
    print("\n=== ELIMINAR PRODUCTO ===")

    try:
        codigo = int(input("Ingrese el código del producto: "))

        restaurante.eliminar_producto(codigo)

    except ValueError:
        print("El código debe ser un número entero.")


def registrar_usuario():
    print("\n=== REGISTRAR USUARIO ===")

    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    if not identificacion.strip() or not nombre.strip() or not correo.strip():
        print("Todos los datos son obligatorios.")
        return

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    restaurante.registrar_usuario(usuario)


def mostrar_menu():
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Mostrar categorías")
    print("9. Salir")


# Menú principal
while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()

    elif opcion == "2":
        buscar_producto()

    elif opcion == "3":
        actualizar_producto()

    elif opcion == "4":
        eliminar_producto()

    elif opcion == "5":
        restaurante.listar_productos()

    elif opcion == "6":
        registrar_usuario()

    elif opcion == "7":
        restaurante.listar_usuarios()

    elif opcion == "8":
        restaurante.mostrar_categorias()

    elif opcion == "9":
        print("\nGracias por utilizar el sistema.")
        break

    else:
        print("\nOpción no válida.")
        