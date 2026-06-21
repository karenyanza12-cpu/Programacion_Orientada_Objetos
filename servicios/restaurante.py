from modelos.producto import Producto
from modelos.cliente import Cliente

# Clase que administra los productos y clientes

class Restaurante:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    # Registrar un nuevo producto
    def agregar_producto(self, nombre, precio):
        producto = Producto(nombre, precio)
        self.productos.append(producto)

    # Registrar un nuevo cliente
    def agregar_cliente(self, nombre, telefono):
        cliente = Cliente(nombre, telefono)
        self.clientes.append(cliente)

    # Mostrar los productos registrados
    def mostrar_productos(self):
        print("Productos registrados:")
        for producto in self.productos:
            print(producto)

    # Mostrar los clientes registrados
    def mostrar_clientes(self):
        print("Clientes registrados:")
        for cliente in self.clientes:
            print(cliente)
            