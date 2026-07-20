# Clase que representa un producto del restaurante

class Producto:

    def __init__(
        self,
        codigo: int,
        nombre: str,
        categoria: str,
        precio: float
    ):

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    # Método para mostrar la información del producto
    def mostrar_informacion(self) -> None:

        print("----------------------------------")
        print("PRODUCTO")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio:.2f}")
        