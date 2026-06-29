from modelos.producto import Producto
from modelos.cliente import Cliente


# Clase que administra el restaurante

class Restaurante:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def mostrar_productos(self) -> None:

        print("\n========== PRODUCTOS ==========")

        for producto in self.productos:
            print(producto)
            print("------------------------------")

    def mostrar_clientes(self) -> None:

        print("\n========== CLIENTES ==========")

        for cliente in self.clientes:
            print(cliente)
            print("------------------------------")

    def vender_producto(self, codigo: int, cantidad: int):

        for producto in self.productos:

            if producto.codigo == codigo:

                if producto.vender_producto(cantidad):
                    print(f"Venta realizada de {producto.nombre}.")
                else:
                    print("No existe suficiente stock.")
                return

        print("Producto no encontrado.")
        