from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


# Clase encargada de administrar los registros
class Restaurante:

    def __init__(self):

        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    # Registrar un producto o bebida
    def registrar_producto(self, producto: Producto) -> bool:

        for producto_registrado in self.productos:

            if producto_registrado.codigo == producto.codigo:
                print("El código ya existe.")
                return False

        self.productos.append(producto)
        print("Producto registrado correctamente.")
        return True

    # Registrar cliente
    def registrar_cliente(self, cliente: Cliente) -> bool:

        for cliente_registrado in self.clientes:

            if cliente_registrado.identificacion == cliente.identificacion:
                print("La identificación ya existe.")
                return False

        self.clientes.append(cliente)
        print("Cliente registrado correctamente.")
        return True

    # Listar productos
    def listar_productos(self) -> None:

        if len(self.productos) == 0:
            print("\nNo existen productos registrados.")
            return

        print("\n========== PRODUCTOS ==========")

        for producto in self.productos:
            producto.mostrar_informacion()

    # Listar clientes
    def listar_clientes(self) -> None:

        if len(self.clientes) == 0:
            print("\nNo existen clientes registrados.")
            return

        print("\n========== CLIENTES ==========")

        for cliente in self.clientes:
            cliente.mostrar_informacion()
            