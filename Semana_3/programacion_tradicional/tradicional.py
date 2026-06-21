# Funcion para registrar una mascota
def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))

    return nombre, especie, edad


# Funcion para mostrar la informacion
def mostrar_informacion(nombre, especie, edad):
    print("\n----- INFORMACION DE LA MASCOTA -----")
    print("Nombre:", nombre)
    print("Especie:", especie)
    print("Edad:", edad, "años")


# Programa principal
print("=== REGISTRO DE MASCOTAS ===")

nombre, especie, edad = registrar_mascota()

mostrar_informacion(nombre, especie, edad)
