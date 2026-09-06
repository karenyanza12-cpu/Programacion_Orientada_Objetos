# Programa principal del sistema Amalia Restaurant
# Semana 12 - Uso de colecciones para mejorar el rendimiento

import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


# ==================================================
# RUTAS DE LOS ARCHIVOS JSON
# ==================================================

CARPETA_PROYECTO = os.path.dirname(
    os.path.abspath(__file__)
)

CARPETA_DATOS = os.path.join(
    CARPETA_PROYECTO,
    "datos"
)

RUTA_PRODUCTOS = os.path.join(
    CARPETA_DATOS,
    "productos.json"
)

RUTA_USUARIOS = os.path.join(
    CARPETA_DATOS,
    "usuarios.json"
)

RUTA_VENTAS = os.path.join(
    CARPETA_DATOS,
    "ventas.json"
)


# Crear carpeta datos si no existe
os.makedirs(
    CARPETA_DATOS,
    exist_ok=True
)


# ==================================================
# CREAR SERVICIOS
# ==================================================

restaurante = Restaurante()

archivo_servicio = ArchivoServicio(
    RUTA_PRODUCTOS,
    RUTA_USUARIOS,
    RUTA_VENTAS
)


# ==================================================
# CARGAR PRODUCTOS
# ==================================================

productos_guardados = (
    archivo_servicio.cargar_productos()
)

for datos in productos_guardados:

    try:

        producto = Producto(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"],
            disponible=datos["disponible"]
        )

        restaurante.agregar_producto(
            producto
        )

    except KeyError as error:

        print(
            f"Advertencia: el producto almacenado "
            f"no contiene la clave {error}. "
            f"Se omitirá este registro."
        )

    except ValueError as error:

        print(
            f"Advertencia: se encontró un producto "
            f"con datos inválidos: {error}. "
            f"Se omitirá este registro."
        )


# ==================================================
# CARGAR USUARIOS
# ==================================================

usuarios_guardados = (
    archivo_servicio.cargar_usuarios()
)

for datos in usuarios_guardados:

    try:

        usuario = Usuario(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"]
        )

        restaurante.agregar_usuario(
            usuario
        )

    except KeyError as error:

        print(
            f"Advertencia: el usuario almacenado "
            f"no contiene la clave {error}. "
            f"Se omitirá este registro."
        )

    except ValueError as error:

        print(
            f"Advertencia: se encontró un usuario "
            f"con datos inválidos: {error}. "
            f"Se omitirá este registro."
        )


# ==================================================
# CARGAR VENTAS
# ==================================================

ventas_guardadas = (
    archivo_servicio.cargar_ventas()
)

for datos in ventas_guardadas:

    try:

        venta = Venta(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=datos["cantidad"]
        )

        restaurante.agregar_venta(
            venta
        )

    except KeyError as error:

        print(
            f"Advertencia: la venta almacenada "
            f"no contiene la clave {error}. "
            f"Se omitirá este registro."
        )

    except ValueError as error:

        print(
            f"Advertencia: se encontró una venta "
            f"con datos inválidos: {error}. "
            f"Se omitirá este registro."
        )


# ==================================================
# RECONSTRUIR ÍNDICES
# ==================================================

restaurante.reconstruir_indices()


# ==================================================
# PRODUCTOS
# ==================================================

def registrar_producto():

    print("\n=== REGISTRAR PRODUCTO ===")

    try:

        codigo = int(
            input("Código: ")
        )

        nombre = input(
            "Nombre: "
        )

        precio = float(
            input("Precio: ")
        )

        stock = int(
            input("Stock: ")
        )

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

        if restaurante.agregar_producto(
            producto
        ):

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print(
                "Producto registrado correctamente."
            )

        else:

            print(
                "El código ya existe."
            )

    except ValueError as error:

        print(
            f"Error: {error}"
        )


def listar_productos():

    print(
        "\n=== PRODUCTOS DEL RESTAURANTE ==="
    )

    print(
        "----------------------------------------"
    )

    productos = (
        restaurante.listar_productos()
    )

    if not productos:

        print(
            "No existen productos registrados."
        )

        return

    for producto in productos:

        print(producto)

        print(
            "----------------------------------------"
        )


def buscar_producto():

    print(
        "\n=== BUSCAR PRODUCTO ==="
    )

    try:

        codigo = int(
            input(
                "Ingrese el código del producto: "
            )
        )

        producto = (
            restaurante.buscar_producto(
                codigo
            )
        )

        if producto is not None:

            print(
                "\nProducto encontrado:"
            )

            print(producto)

        else:

            print(
                "Producto no encontrado."
            )

    except ValueError:

        print(
            "El código debe ser un número."
        )


def actualizar_producto():

    print(
        "\n=== ACTUALIZAR PRODUCTO ==="
    )

    try:

        codigo = int(
            input(
                "Código del producto: "
            )
        )

        producto = (
            restaurante.buscar_producto(
                codigo
            )
        )

        if producto is None:

            print(
                "Producto no encontrado."
            )

            return

        nombre = input(
            "Nuevo nombre: "
        )

        precio = float(
            input(
                "Nuevo precio: "
            )
        )

        stock = int(
            input(
                "Nuevo stock: "
            )
        )

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

            print(
                "Producto actualizado correctamente."
            )

        else:

            print(
                "No se pudo actualizar el producto."
            )

    except ValueError as error:

        print(
            f"Error: {error}"
        )


def eliminar_producto():

    print(
        "\n=== ELIMINAR PRODUCTO ==="
    )

    try:

        codigo = int(
            input(
                "Código del producto: "
            )
        )

        if restaurante.eliminar_producto(
            codigo
        ):

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print(
                "Producto eliminado correctamente."
            )

        else:

            print(
                "Producto no encontrado."
            )

    except ValueError:

        print(
            "El código debe ser un número."
        )


# ==================================================
# USUARIOS
# ==================================================

def registrar_usuario():

    print(
        "\n=== REGISTRAR USUARIO ==="
    )

    try:

        identificacion = input(
            "Identificación: "
        )

        nombre = input(
            "Nombre: "
        )

        correo = input(
            "Correo: "
        )

        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )

        if restaurante.agregar_usuario(
            usuario
        ):

            archivo_servicio.guardar_usuarios(
                restaurante.usuarios
            )

            print(
                "Usuario registrado correctamente."
            )

        else:

            print(
                "La identificación ya está registrada."
            )

    except ValueError as error:

        print(
            f"Error: {error}"
        )


def listar_usuarios():

    print(
        "\n=== USUARIOS REGISTRADOS ==="
    )

    print(
        "----------------------------------------"
    )

    usuarios = (
        restaurante.listar_usuarios()
    )

    if not usuarios:

        print(
            "No existen usuarios registrados."
        )

        return

    for usuario in usuarios:

        print(usuario)

        print(
            "----------------------------------------"
        )


def buscar_usuario():

    print(
        "\n=== BUSCAR USUARIO ==="
    )

    identificacion = input(
        "Ingrese la identificación: "
    )

    usuario = (
        restaurante.buscar_usuario(
            identificacion
        )
    )

    if usuario is not None:

        print(
            "\nUsuario encontrado:"
        )

        print(usuario)

    else:

        print(
            "Usuario no encontrado."
        )


# ==================================================
# VENTAS
# ==================================================

def vender_producto():

    print(
        "\n=== REALIZAR VENTA ==="
    )

    try:

        identificacion = input(
            "Identificación del usuario: "
        )

        codigo = int(
            input(
                "Código del producto: "
            )
        )

        cantidad = int(
            input(
                "Cantidad: "
            )
        )

        usuario = (
            restaurante.buscar_usuario(
                identificacion
            )
        )

        if usuario is None:

            print(
                "No se puede realizar la venta: "
                "el usuario no existe."
            )

            return

        producto = (
            restaurante.buscar_producto(
                codigo
            )
        )

        if producto is None:

            print(
                "No se puede realizar la venta: "
                "el producto no existe."
            )

            return

        if cantidad <= 0:

            print(
                "La cantidad debe ser mayor que cero."
            )

            return

        if producto.stock < cantidad:

            print(
                "No se puede realizar la venta: "
                "stock insuficiente."
            )

            print(
                f"Stock disponible: {producto.stock}"
            )

            return

        if not producto.disponible:

            print(
                "No se puede realizar la venta: "
                "el producto no está disponible."
            )

            return

        stock_anterior = producto.stock

        if restaurante.vender_producto(
            codigo,
            identificacion,
            cantidad
        ):

            archivo_servicio.guardar_ventas(
                restaurante.ventas
            )

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print(
                "\nVenta realizada correctamente."
            )

            print(
                f"Producto: {producto.nombre}"
            )

            print(
                f"Cantidad vendida: {cantidad}"
            )

            print(
                f"Stock anterior: {stock_anterior}"
            )

            print(
                f"Stock actual: {producto.stock}"
            )

        else:

            print(
                "No se pudo realizar la venta."
            )

    except ValueError:

        print(
            "Ingrese valores numéricos válidos."
        )


def consultar_ventas_usuario():

    print(
        "\n=== VENTAS DE UN USUARIO ==="
    )

    identificacion = input(
        "Ingrese la identificación del usuario: "
    )

    usuario = (
        restaurante.buscar_usuario(
            identificacion
        )
    )

    if usuario is None:

        print(
            "Usuario no encontrado."
        )

        return

    ventas = (
        restaurante.consultar_ventas_usuario(
            identificacion
        )
    )

    print(
        f"\nVentas realizadas por: "
        f"{usuario.nombre}"
    )

    print(
        "----------------------------------------"
    )

    if not ventas:

        print(
            "Este usuario no tiene ventas registradas."
        )

        return

    for venta in ventas:

        producto = (
            restaurante.buscar_producto(
                venta.producto_codigo
            )
        )

        if producto is not None:

            print(
                f"Producto: {producto.nombre}"
            )

        else:

            print(
                f"Producto código: "
                f"{venta.producto_codigo}"
            )

        print(
            f"Código del producto: "
            f"{venta.producto_codigo}"
        )

        print(
            f"Cantidad: {venta.cantidad}"
        )

        print(
            "----------------------------------------"
        )


# ==================================================
# MENÚ
# ==================================================

def mostrar_menu():

    print(
        "\n========================================"
    )

    print(
        "          AMALIA RESTAURANT"
    )

    print(
        "             SEMANA 12"
    )

    print(
        "========================================"
    )

    print(
        "1. Registrar producto"
    )

    print(
        "2. Listar productos"
    )

    print(
        "3. Buscar producto"
    )

    print(
        "4. Actualizar producto"
    )

    print(
        "5. Eliminar producto"
    )

    print(
        "----------------------------------------"
    )

    print(
        "6. Registrar usuario"
    )

    print(
        "7. Listar usuarios"
    )

    print(
        "8. Buscar usuario"
    )

    print(
        "----------------------------------------"
    )

    print(
        "9. Realizar venta"
    )

    print(
        "10. Consultar ventas por usuario"
    )

    print(
        "----------------------------------------"
    )

    print(
        "11. Salir"
    )


# ==================================================
# MENÚ PRINCIPAL
# ==================================================

while True:

    mostrar_menu()

    opcion = input(
        "Seleccione una opción: "
    )

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

        registrar_usuario()

    elif opcion == "7":

        listar_usuarios()

    elif opcion == "8":

        buscar_usuario()

    elif opcion == "9":

        vender_producto()

    elif opcion == "10":

        consultar_ventas_usuario()

    elif opcion == "11":

        print(
            "\nGracias por utilizar "
            "Amalia Restaurant."
        )

        break

    else:

        print(
            "Opción no válida."
        )
        