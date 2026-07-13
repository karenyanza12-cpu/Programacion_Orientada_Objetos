# Clase que representa un producto del restaurante

class Producto:

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool):

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # Propiedad para el nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):

        if nuevo_nombre.strip() != "":
            self.__nombre = nuevo_nombre
        else:
            print("El nombre no puede estar vacío.")
            self.__nombre = "Sin nombre"

    # Propiedad para la categoría
    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nueva_categoria):

        if nueva_categoria.strip() != "":
            self.__categoria = nueva_categoria
        else:
            print("La categoría no puede estar vacía.")
            self.__categoria = "Sin categoría"

    # Propiedad para el precio
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):

        if nuevo_precio > 0: 
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que cero.")
            self.__precio = 1.00

    # Mostrar información del producto
    def mostrar_informacion(self):
        
        estado = "Disponible" if self.disponible else "No disponible"
        print("-------------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Estado: {estado}")
