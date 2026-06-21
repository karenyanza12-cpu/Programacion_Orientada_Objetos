from clase import Estudiante_Clase

estudiante1 = Estudiante_Clase(
    "1150978728",
    "Kerly Yanza",
    "Tecnologías de la Información",
    20
)

estudiante2 = Estudiante_Clase(
    "1101234567",
    "Maria Lopez",
    "Tecnologías de la Información",
    21
)

estudiante1.saludar_impreso()
estudiante1.estudiar()

print("-------------------")

estudiante2.saludar_impreso()
estudiante2.estudiar()
