from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


# Crear restaurante
restaurante = Restaurante("Amalia Restaurant")


# Crear platillos
platillo1 = Platillo(
    "Sándwich de Pollo",
    3.50,
    True,
    "Comida rápida"
)

platillo2 = Platillo(
    "Especial Amalia",
    7.50,
    True,
    "Plato fuerte"
)


# Crear bebidas
bebida1 = Bebida(
    "Frappé de Nutella",
    3.00,
    True,
    "Grande"
)

bebida2 = Bebida(
    "Limonada de Hierbabuena",
    2.50,
    True,
    "Mediana"
)


# Agregar productos al restaurante
restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)


# Mostrar todos los productos
restaurante.mostrar_productos()


# Demostración de encapsulación
print("\nPrecio actual del Especial Amalia:")
print(f"${platillo2.obtener_precio():.2f}")

print("\nSe cambia el precio del Especial Amalia...\n")

platillo2.cambiar_precio(8.00)

print("Nuevo precio:")
print(f"${platillo2.obtener_precio():.2f}")
