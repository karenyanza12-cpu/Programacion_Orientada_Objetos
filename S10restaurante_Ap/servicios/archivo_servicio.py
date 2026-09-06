# Servicio encargado de guardar y cargar productos desde un archivo JSON

import json


class ArchivoServicio:

    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo

    def guardar_productos(self, productos) -> None:
        """Guarda los productos en el archivo JSON."""

        datos = []

        for producto in productos:
            datos.append(producto.to_dict())

        try:
            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print(
                "Error: no existen permisos para escribir "
                "en el archivo de productos."
            )

    def cargar_productos(self) -> list:
        """Carga los productos almacenados en el archivo JSON."""

        try:
            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                if not isinstance(datos, list):
                    print(
                        "Error: el archivo JSON debe contener "
                        "una lista de productos."
                    )
                    return []

                return datos

        except FileNotFoundError:
            print(
                "Aviso: todavía no existe productos.json. "
                "Se iniciará con una lista vacía."
            )
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json contiene información "
                "que no tiene un formato JSON válido."
            )
            return []

        except PermissionError:
            print(
                "Error: no existen permisos para leer "
                "el archivo de productos."
            )
            return []
        
        