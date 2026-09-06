# Programa principal del sistema Amalia Restaurant

import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


# Ruta absoluta del archivo donde se guardan los productos
CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))

RUTA_PRODUCTOS = os.path.join(
    CARPETA_PROYECTO,
    "datos",
    "productos.json"
)


# Crear los servicios principales
restaurante = Restaurante()
archivo_servicio = ArchivoServicio(RUTA_PRODUCTOS)


# Cargar los productos guardados anteriormente
productos_guardados = archivo_servicio.cargar_productos()

for datos in productos_guardados:

    try:
        producto = Producto(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"],
            disponible=datos["disponible"]
        )

        restaurante.agregar_producto(producto)

    except KeyError as error:
        print(
            f"Advertencia: el producto almacenado no contiene "
            f"la clave {error}. Se omitirá este registro."
        )

    except ValueError as error:
        print(
            f"Advertencia: se encontró un producto con datos "
            f"inválidos: {error}. Se omitirá este registro."
        )


def registrar_producto():
    print("\n=== REGISTRAR PRODUCTO ===")

    try:
        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        disponible = input(
            "¿Está disponible? (s/n): "
        ).lower() == "s"

        producto = Producto(
            codigo,
            nombre,
            precio,
            stock,
            disponible
        )

        if restaurante.agregar_producto(producto):

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print("Producto registrado correctamente.")

        else:
            print("El código ya existe.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_productos():
    print("\n=== PRODUCTOS DEL RESTAURANTE ===")
    print("----------------------------------------")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)
        print("----------------------------------------")


def buscar_producto():
    print("\n=== BUSCAR PRODUCTO ===")

    try:
        codigo = int(
            input("Ingrese el código del producto: ")
        )

        producto = restaurante.buscar_producto(codigo)

        if producto is not None:
            print("\nProducto encontrado:")
            print(producto)

        else:
            print("Producto no encontrado.")

    except ValueError:
        print("El código debe ser un número.")


def actualizar_producto():
    print("\n=== ACTUALIZAR PRODUCTO ===")

    try:
        codigo = int(
            input("Código del producto: ")
        )

        producto = restaurante.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return

        nombre = input("Nuevo nombre: ")
        precio = float(input("Nuevo precio: "))
        stock = int(input("Nuevo stock: "))

        disponible = input(
            "¿Está disponible? (s/n): "
        ).lower() == "s"

        if restaurante.actualizar_producto(
            codigo,
            nombre,
            precio,
            stock,
            disponible
        ):

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print("Producto actualizado correctamente.")

        else:
            print("No se pudo actualizar el producto.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto():
    print("\n=== ELIMINAR PRODUCTO ===")

    try:
        codigo = int(
            input("Código del producto: ")
        )

        if restaurante.eliminar_producto(codigo):

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print("Producto eliminado correctamente.")

        else:
            print("Producto no encontrado.")

    except ValueError:
        print("El código debe ser un número.")


def vender_producto():
    print("\n=== REALIZAR VENTA ===")

    try:
        codigo = int(
            input("Código del producto: ")
        )

        cantidad = int(
            input("Cantidad: ")
        )

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        if restaurante.vender_producto(codigo, cantidad):

            # Guardar el nuevo stock en el archivo JSON
            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print("Venta realizada correctamente.")

        else:
            print(
                "No se pudo realizar la venta. "
                "Verifique el producto, disponibilidad o stock."
            )

    except ValueError:
        print("Ingrese valores numéricos válidos.")


def registrar_usuario():
    print("\n=== REGISTRAR USUARIO ===")

    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.agregar_usuario(usuario):
        print("Usuario registrado correctamente.")

    else:
        print("La identificación ya está registrada.")


def listar_usuarios():
    print("\n=== USUARIOS REGISTRADOS ===")
    print("----------------------------------------")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)
        print("----------------------------------------")


def buscar_usuario():
    print("\n=== BUSCAR USUARIO ===")

    identificacion = input(
        "Ingrese la identificación: "
    )

    usuario = restaurante.buscar_usuario(
        identificacion
    )

    if usuario is not None:
        print("\nUsuario encontrado:")
        print(usuario)

    else:
        print("Usuario no encontrado.")


def mostrar_menu():

    print("\n========================================")
    print("          AMALIA RESTAURANT")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Realizar venta")
    print("----------------------------------------")
    print("7. Registrar usuario")
    print("8. Listar usuarios")
    print("9. Buscar usuario")
    print("----------------------------------------")
    print("10. Salir")


# Menú principal
while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()

    elif opcion == "2":
        listar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        actualizar_producto()

    elif opcion == "5":
        eliminar_producto()

    elif opcion == "6":
        vender_producto()

    elif opcion == "7":
        registrar_usuario()

    elif opcion == "8":
        listar_usuarios()

    elif opcion == "9":
        buscar_usuario()

    elif opcion == "10":
        print("\nGracias por utilizar Amalia Restaurant.")
        break

    else:
        print("Opción no válida.")
        