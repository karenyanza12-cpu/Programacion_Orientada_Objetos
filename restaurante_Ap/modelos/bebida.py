from modelos.producto import Producto


# Clase hija de Producto

class Bebida(Producto):

    def __init__(
        self,
        codigo: int,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str
    ):

        super().__init__(
            codigo,
            nombre,
            categoria,
            precio
        )

        self.tamano = tamano

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self) -> None:

        print("----------------------------------")
        print("BEBIDA")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Tamaño: {self.tamano}")
        