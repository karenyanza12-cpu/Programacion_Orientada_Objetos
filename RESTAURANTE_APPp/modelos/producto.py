# Clase que representa un producto del restaurante

class Producto:

    def __init__(self, codigo: int, nombre: str, precio: float, stock: int, disponible: bool):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.disponible = disponible

    def vender_producto(self, cantidad: int) -> bool:
        """Reduce el stock cuando se realiza una venta."""

        if self.disponible and self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Código: {self.codigo}\n"
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Stock: {self.stock}\n"
            f"Estado: {estado}"
        )
    