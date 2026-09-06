# Clase encargada de administrar productos, usuarios y ventas
# Semana 12 - Uso de colecciones para mejorar el rendimiento

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:

    def __init__(self):

        # Colecciones principales
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []

        # Índice de productos por código
        self.indice_productos: dict[int, Producto] = {}

        # Índice de usuarios por identificación
        self.indice_usuarios: dict[str, Usuario] = {}

        # Índice de ventas agrupadas por usuario
        self.ventas_por_usuario: dict[str, list[Venta]] = {}

    # ==================================================
    # RECONSTRUIR ÍNDICES
    # ==================================================

    def reconstruir_indices(self) -> None:
        """
        Reconstruye los índices auxiliares utilizando
        las colecciones principales.
        """

        self.indice_productos.clear()
        self.indice_usuarios.clear()
        self.ventas_por_usuario.clear()

        for producto in self.productos:
            self.indice_productos[producto.codigo] = producto

        for usuario in self.usuarios:
            self.indice_usuarios[
                usuario.identificacion
            ] = usuario

        for venta in self.ventas:

            if venta.usuario_id not in self.ventas_por_usuario:
                self.ventas_por_usuario[
                    venta.usuario_id
                ] = []

            self.ventas_por_usuario[
                venta.usuario_id
            ].append(venta)

    # ==================================================
    # PRODUCTOS
    # ==================================================

    def agregar_producto(
        self,
        producto: Producto
    ) -> bool:
        """Agrega un producto y actualiza su índice."""

        if producto.codigo in self.indice_productos:
            return False

        self.productos.append(producto)

        self.indice_productos[
            producto.codigo
        ] = producto

        return True

    def listar_productos(self) -> list[Producto]:
        """Devuelve la colección principal de productos."""

        return self.productos

    def buscar_producto(self, codigo: int):
        """
        Busca un producto utilizando el índice
        por código.
        """

        return self.indice_productos.get(codigo)

    def actualizar_producto(
        self,
        codigo: int,
        nombre: str,
        precio: float,
        stock: int,
        disponible: bool
    ) -> bool:
        """Actualiza la información de un producto."""

        producto = self.indice_productos.get(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.disponible = disponible

        return True

    def eliminar_producto(
        self,
        codigo: int
    ) -> bool:
        """Elimina un producto y actualiza su índice."""

        producto = self.indice_productos.get(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)

        del self.indice_productos[codigo]

        return True

    # ==================================================
    # USUARIOS
    # ==================================================

    def agregar_usuario(
        self,
        usuario: Usuario
    ) -> bool:
        """Agrega un usuario y actualiza su índice."""

        if usuario.identificacion in self.indice_usuarios:
            return False

        self.usuarios.append(usuario)

        self.indice_usuarios[
            usuario.identificacion
        ] = usuario

        return True

    def listar_usuarios(self) -> list[Usuario]:
        """Devuelve la colección principal de usuarios."""

        return self.usuarios

    def buscar_usuario(
        self,
        identificacion: str
    ):
        """
        Busca un usuario utilizando el índice
        por identificación.
        """

        return self.indice_usuarios.get(
            identificacion
        )

    # ==================================================
    # VENTAS
    # ==================================================

    def agregar_venta(
        self,
        venta: Venta
    ) -> None:
        """
        Agrega una venta a la lista principal y
        actualiza el índice de ventas por usuario.
        """

        self.ventas.append(venta)

        if venta.usuario_id not in self.ventas_por_usuario:
            self.ventas_por_usuario[
                venta.usuario_id
            ] = []

        self.ventas_por_usuario[
            venta.usuario_id
        ].append(venta)

    def vender_producto(
        self,
        codigo_producto: int,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:
        """
        Realiza una venta relacionando un usuario
        con un producto.
        """

        # Buscar usuario utilizando el índice
        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        # Buscar producto utilizando el índice
        producto = self.buscar_producto(
            codigo_producto
        )

        # Validar que existan
        if usuario is None or producto is None:
            return False

        # Validar cantidad
        if cantidad <= 0:
            return False

        # Validar stock
        if producto.stock < cantidad:
            return False

        # Validar disponibilidad
        if not producto.disponible:
            return False

        # Crear venta
        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        # Actualizar stock
        if not producto.vender_producto(cantidad):
            return False

        # Registrar venta y actualizar índice
        self.agregar_venta(venta)

        return True

    def listar_ventas(self) -> list[Venta]:
        """Devuelve todas las ventas."""

        return self.ventas

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:
        """
        Consulta las ventas de un usuario mediante
        el índice de ventas por usuario.
        """

        return self.ventas_por_usuario.get(
            identificacion_usuario,
            []
        )
    