from modelos.producto import Producto


# Clase que administra los productos del restaurante

class Restaurante:

    def __init__(self, nombre: str):

        self.nombre = nombre
        self.productos = []

    # Agrega un producto a la lista
    def agregar_producto(self, producto: Producto) -> None:

        self.productos.append(producto)

    # Muestra todos los productos registrados
    def mostrar_productos(self) -> None:

        print("\n===================================")
        print(f"      {self.nombre.upper()}")
        print("===================================\n")

        for producto in self.productos:

            producto.mostrar_informacion()
            print("-------------------------------")
            