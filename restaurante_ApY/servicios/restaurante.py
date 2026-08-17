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

        producto.actualizar(
            nombre,
            categoria,
            precio,
            disponible
        )

        self.categorias.add(categoria)

        print("Producto actualizado correctamente.")
        return True

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        self.productos.remove(producto)

        self.actualizar_categorias()

        print("Producto eliminado correctamente.")
        return True

    def listar_productos(self):
        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\n========== PRODUCTOS ==========")

        for producto in self.productos:
            producto.mostrar_informacion()

    # ---------------- USUARIOS ----------------

    def registrar_usuario(self, usuario):
        for usuario_registrado in self.usuarios:
            if usuario_registrado.identificacion == usuario.identificacion:
                print("La identificación ya está registrada.")
                return False

        self.usuarios.append(usuario)

        print("Usuario registrado correctamente.")
        return True

    def listar_usuarios(self):
        if not self.usuarios:
            print("No existen usuarios registrados.")
            return

        print("\n========== USUARIOS ==========")

        for usuario in self.usuarios:
            print("----------------------------------------")
            print(f"Identificación: {usuario.identificacion}")
            print(f"Nombre: {usuario.nombre}")
            print(f"Correo: {usuario.correo}")

    def buscar_usuario(self, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    # ---------------- CATEGORÍAS ----------------

    def actualizar_categorias(self):
        self.categorias.clear()

        for producto in self.productos:
            self.categorias.add(producto.categoria)

    def mostrar_categorias(self):
        if not self.categorias:
            print("No existen categorías registradas.")
            return

        print("\n========== CATEGORÍAS ==========")

        for categoria in sorted(self.categorias):
            print(f"- {categoria}")