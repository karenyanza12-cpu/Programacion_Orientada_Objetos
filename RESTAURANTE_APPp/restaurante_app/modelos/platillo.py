from modelos.producto import Producto


# Clase hija Platillo

class Platillo(Producto):

    def __init__(self,
                 nombre: str,
                 precio: float,
                 disponible: bool,
                 tipo_platillo: str):

        super().__init__(nombre, precio, disponible)

        self.tipo_platillo = tipo_platillo

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self) -> None:

        estado = "Disponible" if self.disponible else "No disponible"

        print("------ PLATILLO ------")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Tipo: {self.tipo_platillo}")
        print(f"Estado: {estado}")
        