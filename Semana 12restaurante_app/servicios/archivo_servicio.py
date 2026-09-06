# Servicio encargado de guardar y cargar información mediante JSON

import json


class ArchivoServicio:

    def __init__(
        self,
        ruta_productos: str,
        ruta_usuarios: str,
        ruta_ventas: str
    ):
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas

    # ==================================================
    # PRODUCTOS
    # ==================================================

    def guardar_productos(self, productos) -> None:

        datos = []

        for producto in productos:
            datos.append(producto.to_dict())

        try:
            with open(
                self.ruta_productos,
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
                "en productos.json."
            )

    def cargar_productos(self) -> list:

        try:
            with open(
                self.ruta_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                if not isinstance(datos, list):
                    print(
                        "Error: productos.json debe contener "
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
                "productos.json."
            )
            return []

    # ==================================================
    # USUARIOS
    # ==================================================

    def guardar_usuarios(self, usuarios) -> None:

        datos = []

        for usuario in usuarios:
            datos.append(usuario.to_dict())

        try:
            with open(
                self.ruta_usuarios,
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
                "en usuarios.json."
            )

    def cargar_usuarios(self) -> list:

        try:
            with open(
                self.ruta_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                if not isinstance(datos, list):
                    print(
                        "Error: usuarios.json debe contener "
                        "una lista de usuarios."
                    )
                    return []

                return datos

        except FileNotFoundError:
            print(
                "Aviso: todavía no existe usuarios.json. "
                "Se iniciará con una lista vacía."
            )
            return []

        except json.JSONDecodeError:
            print(
                "Error: usuarios.json contiene información "
                "que no tiene un formato JSON válido."
            )
            return []

        except PermissionError:
            print(
                "Error: no existen permisos para leer "
                "usuarios.json."
            )
            return []

    # ==================================================
    # VENTAS
    # ==================================================

    def guardar_ventas(self, ventas) -> None:

        datos = []

        for venta in ventas:
            datos.append(venta.to_dict())

        try:
            with open(
                self.ruta_ventas,
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
                "en ventas.json."
            )

    def cargar_ventas(self) -> list:

        try:
            with open(
                self.ruta_ventas,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                if not isinstance(datos, list):
                    print(
                        "Error: ventas.json debe contener "
                        "una lista de ventas."
                    )
                    return []

                return datos

        except FileNotFoundError:
            print(
                "Aviso: todavía no existe ventas.json. "
                "Se iniciará con una lista vacía."
            )
            return []

        except json.JSONDecodeError:
            print(
                "Error: ventas.json contiene información "
                "que no tiene un formato JSON válido."
            )
            return []

        except PermissionError:
            print(
                "Error: no existen permisos para leer "
                "ventas.json."
            )
            return []
        