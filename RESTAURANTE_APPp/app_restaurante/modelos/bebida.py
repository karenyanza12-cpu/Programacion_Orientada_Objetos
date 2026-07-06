from modelos.producto import Producto


# Clase hija Bebida

class Bebida(Producto):

    def __init__(self,
                 nombre: str,
                 precio: float,
                 disponible: bool,
                 tamano: str):

        super().__init__(nombre, precio, disponible)

        self.tamano = tamano

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self) -> None:

        estado = "Disponible" if self.disponible else "No disponible"

        print("------ BEBIDA ------")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Tamaño: {self.tamano}")
        print(f"Estado: {estado}")
        