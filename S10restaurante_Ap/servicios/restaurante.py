# Clase encargada de administrar los productos y usuarios

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:

    def __init__(self):
        self.productos = []
        self.usuarios = []

    # ---------------- PRODUCTOS ----------------

    def agregar_producto(self, producto: Producto) -> bool:
        """Agrega un producto a la lista."""

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)
        return True

    def listar_productos(self):
        """Devuelve la lista de productos."""

        return self.productos

    def buscar_producto(self, codigo: int):
        """Busca un producto por su código."""

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: int,
        nombre: str,
        precio: float,
        stock: int,
        disponible: bool
    ) -> bool:
        """Actualiza la información de un producto."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.disponible = disponible

        return True

    def eliminar_producto(self, codigo: int) -> bool:
        """Elimina un producto de la lista."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True

    def vender_producto(self, codigo: int, cantidad: int) -> bool:
        """Realiza una venta de un producto."""

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        return producto.vender_producto(cantidad)

    # ---------------- USUARIOS ----------------

    def agregar_usuario(self, usuario: Usuario) -> bool:
        """Agrega un usuario al restaurante."""

        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self):
        """Devuelve la lista de usuarios."""

        return self.usuarios

    def buscar_usuario(self, identificacion: str):
        """Busca un usuario por su identificación."""

        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None
    