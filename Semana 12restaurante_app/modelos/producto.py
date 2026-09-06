# Clase que representa un producto del restaurante


class Producto:

    def __init__(
        self,
        codigo: int,
        nombre: str,
        precio: float,
        stock: int,
        disponible: bool
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.disponible = disponible

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor <= 0:
            raise ValueError(
                "El código debe ser mayor que cero."
            )

        self._codigo = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        self._stock = valor

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = bool(valor)

    def vender_producto(self, cantidad: int) -> bool:
        """Reduce el stock cuando se realiza una venta."""

        if cantidad <= 0:
            return False

        if self.disponible and self.stock >= cantidad:
            self.stock -= cantidad

            if self.stock == 0:
                self.disponible = False

            return True

        return False

    def __str__(self) -> str:
        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"Código: {self.codigo}\n"
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Stock: {self.stock}\n"
            f"Estado: {estado}"
        )

    def to_dict(self):
        """Convierte el producto en un diccionario para JSON."""

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "disponible": self.disponible
        }
    