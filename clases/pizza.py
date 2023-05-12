from clases.Alimentos import Alimentos
class Pizza(Alimentos):
    def __init__(self, nombre, precio, ingredientes):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes

    def descripcion(self):
        return(f"La {self.nombre} tiene los siguientes ingredientes: {self.ingredientes}. Su precio es {self.precio}.")
