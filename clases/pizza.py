from clases import alimentos
class Pizza(Alimentos):
    def __init__(self, nombre, precio, ingredientes):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes

    def descripcion(self):
        print(f"La pizza {self.nombre} tiene los siguientes ingredientes: {self.ingredientes}. Su precio es {self.precio}.")
