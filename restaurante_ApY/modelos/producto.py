class Producto:
    def __init__(self, codigo: int, nombre: str, categoria: str, precio: float, disponible: bool = True):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print("----------------------------------------")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Estado: {estado}")

    def actualizar(self, nombre: str, categoria: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible
        