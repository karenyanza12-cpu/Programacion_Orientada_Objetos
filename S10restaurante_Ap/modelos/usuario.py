from dataclasses import dataclass


@dataclass
class Usuario:
    identificacion: str
    nombre: str
    correo: str

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )
    