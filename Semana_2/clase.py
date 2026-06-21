class Estudiante_Clase:

    def __init__(self, cedula:str, nombre:str, carrera:str,
                 edad:int):
        self.cedula = cedula
        self.nombre = nombre
        self.carrera = carrera
        self.edad = edad

    def saludar_impreso(self):
        print(f"Hola mi nombre es {self.nombre}, mi cedula es {self.cedula}, estudio la carrera de {self.carrera} y tengo {self.edad} años")

    def estudiar(self):
        print(f"{self.nombre} estudia la carrera de {self.carrera}")
        