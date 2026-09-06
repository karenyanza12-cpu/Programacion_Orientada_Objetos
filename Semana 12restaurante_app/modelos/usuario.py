from dataclasses import dataclass


@dataclass
class Usuario:

    identificacion: str
    nombre: str
    correo: str

    def __post_init__(self):

        if not self.identificacion.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not self.nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not self.correo.strip():
            raise ValueError(
                "El correo no puede estar vacío."
            )

    def mostrar_informacion(self):

        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def to_dict(self):
        """Convierte el usuario en un diccionario para JSON."""

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    def __str__(self) -> str:
        return self.mostrar_informacion()
    