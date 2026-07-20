# Clase que representa un cliente

class Cliente:

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ):

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    # Mostrar información del cliente
    def mostrar_informacion(self) -> None:

        print("----------------------------------")
        print("CLIENTE")
        print(f"Identificación: {self.identificacion}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        