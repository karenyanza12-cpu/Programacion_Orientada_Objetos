# Clase que representa un cliente del restaurante

class Cliente:

    def __init__(self, cedula: str, nombre: str, edad: int, puntos: int, activo: bool):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.puntos = puntos
        self.activo = activo

    def agregar_puntos(self, puntos: int) -> None:
        """Incrementa los puntos del cliente."""
        self.puntos += puntos

    def __str__(self) -> str:
        estado = "Activo" if self.activo else "Inactivo"

        return (
            f"Cédula: {self.cedula}\n"
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Puntos: {self.puntos}\n"
            f"Estado: {estado}"
        )
    