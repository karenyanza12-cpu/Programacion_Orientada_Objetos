from dataclasses import dataclass

# Clase Cliente utilizando @dataclass

@dataclass
class Cliente:

    id_cliente: int
    nombre: str
    correo: str

    def mostrar_informacion(self):

        print("-------------------------------")
        print(f"ID: {self.id_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")

        