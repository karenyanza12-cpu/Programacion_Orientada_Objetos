# Clase padre que representa un producto del restaurante

class Producto:

    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.__precio = precio
        self.disponible = disponible

    # Método para obtener el precio
    def obtener_precio(self) -> float:
        return self.__precio

    # Método para cambiar el precio
    def cambiar_precio(self, nuevo_precio: float) -> None:

        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que cero.")

    # Método que será sobrescrito por las clases hijas
    def mostrar_informacion(self) -> None:

        estado = "Disponible" if self.disponible else "No disponible"

        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Estado: {estado}")
        