from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear restaurante
restaurante = Restaurante("Amalia Restaurant")


# Crear productos
producto1 = Producto(
    1,
    "Sándwich de Pollo",
    3.50,
    20,
    True
)

producto2 = Producto(
    2,
    "Frappé de Nutella",
    3.00,
    15,
    True
)


# Crear clientes
cliente1 = Cliente(
    "1150968227",
    "Ariana",
    19,
    10,
    True
)

cliente2 = Cliente(
    "1150508629",
    "Lia",
    25,
    5,
    True
)


# Registrar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Registrar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("========================================")
print("     AMALIA RESTAURANT")
print("========================================")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()

# Realizar una venta
print("\nRealizando una venta...\n")

restaurante.vender_producto(1, 2)

print("\nProductos después de la venta:")

restaurante.mostrar_productos()
