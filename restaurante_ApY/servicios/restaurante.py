class Restaurante:
    def __init__(self):
        # Lista para almacenar los productos
        self.productos = []

        # Lista para almacenar los usuarios
        self.usuarios = []

        # Tupla con las opciones del menú
        self.opciones_menu = (
            "Registrar producto",
            "Buscar producto",
            "Actualizar producto",
            "Eliminar producto",
            "Listar productos",
            "Registrar usuario",
            "Listar usuarios",
            "Mostrar categorías",
            "Salir"
        )

        # Diccionario para relacionar opciones
        self.opciones = {}

        # Set para almacenar categorías sin repetir
        self.categorias = set()

    # ---------------- PRODUCTOS ----------------

    def registrar_producto(self, producto):
        if self.buscar_producto(producto.codigo) is not None:
            print("El código del producto ya existe.")
            return False

        self.productos.append(producto)
        self.categorias.add(producto.categoria)

        print("Producto registrado correctamente.")
        return True

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        disponible
    ):
        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        producto.actualizar(nombre, categoria, precio, disponible)
        self.categorias.add(categoria)
        print("Producto actualizado correctamente.")
        return True

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        self.productos.remove(producto)
        print("Producto eliminado correctamente.")
        return True

    def listar_productos(self):
        if not self.productos:
            print("\nNo hay productos registrados.")
            return

        for producto in self.productos:
            producto.mostrar_informacion()

    # ---------------- USUARIOS ----------------

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print("Usuario registrado correctamente.")
        return True

    def listar_usuarios(self):
        if not self.usuarios:
            print("\nNo hay usuarios registrados.")
            return

        print("\n=== LISTA DE USUARIOS ===")
        for u in self.usuarios:
            print(f"ID: {u.identificacion} | Nombre: {u.nombre} | Correo: {u.correo}")

    # ---------------- CATEGORÍAS ----------------

    def mostrar_categorias(self):
        if not self.categorias:
            print("\nNo hay categorías registradas.")
            return

        print("\n=== CATEGORÍAS ÚNICAS ===")
        for cat in self.categorias:
            print(f"- {cat}")
            