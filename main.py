from servicios.restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante("Amalia Restaurant")

# Registrar productos
restaurante.agregar_producto("Humitas", 1.25)
restaurante.agregar_producto("Bolón de Verde", 3.00)
restaurante.agregar_producto("Café", 1.00)

# Registrar clientes
restaurante.agregar_cliente("Ariana Peralta", "0991234567")
restaurante.agregar_cliente("Tabita Matute", "987654321")

# Mostrar la información
print("AMALIA RESTAURANT")
print("----------------------")

restaurante.mostrar_productos()

print()

restaurante.mostrar_clientes()