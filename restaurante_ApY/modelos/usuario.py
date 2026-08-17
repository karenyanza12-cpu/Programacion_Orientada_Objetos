from dataclasses import dataclass


@dataclass
class Usuario:
    identificacion: str
    nombre: str
    correo: str
    