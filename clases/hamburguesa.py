from clases.Alimentos import Alimentos
class Hamburguesa(Alimentos):
    def __init__(self, nombre, precio, tipo_carne):
        super().__init__(nombre, precio)
        self.tipo_carne = tipo_carne

    def descripcion(self):
        return(f"La {self.nombre} está hecha con carne de {self.tipo_carne}. Su precio es {self.precio}.")