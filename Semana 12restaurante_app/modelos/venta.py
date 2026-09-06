class Venta:

    def __init__(
        self,
        usuario_id: str,
        producto_codigo: int,
        cantidad: int
    ):

        if not usuario_id.strip():
            raise ValueError(
                "La identificación del usuario no puede estar vacía."
            )

        if producto_codigo <= 0:
            raise ValueError(
                "El código del producto debe ser mayor que cero."
            )

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def to_dict(self):
        """Convierte la venta en un diccionario para JSON."""

        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    def __str__(self) -> str:

        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )
    