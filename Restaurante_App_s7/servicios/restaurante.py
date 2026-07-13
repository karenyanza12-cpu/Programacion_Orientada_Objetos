from modelos.producto import Producto
from modelos.cliente import Cliente


# Clase que administra los productos y clientes

class Restaurante:

    def __init__(self):

        self.productos = []
        self.clientes = []

    # Registrar producto
    def registrar_producto(self, producto: Producto):

        self.productos.append(producto)
        print("Producto registrado correctamente.")

    # Registrar cliente
    def registrar_cliente(self, cliente: Cliente):

        self.clientes.append(cliente)
        print("Cliente registrado correctamente.")

    # Listar productos
    def listar_productos(self):

        if len(self.productos) == 0:
            print("No existen productos registrados.")
            return

        print("\n====== PRODUCTOS ======")

        for producto in self.productos:
            producto.mostrar_informacion()

    # Listar clientes
    def listar_clientes(self):

        if len(self.clientes) == 0:
            print("No existen clientes registrados.")
            return

        print("\n====== CLIENTES ======")

        for cliente in self.clientes:
            cliente.mostrar_informacion()

    # Buscar producto
    def buscar_producto(self, nombre):

        for producto in self.productos:

            if producto.nombre.lower() == nombre.lower():

                producto.mostrar_informacion()
                return

        print("Producto no encontrado.")

    # Buscar cliente
    def buscar_cliente(self, nombre):

        for cliente in self.clientes:

            if cliente.nombre.lower() == nombre.lower():

                cliente.mostrar_informacion()
                return

        print("Cliente no encontrado.")
        