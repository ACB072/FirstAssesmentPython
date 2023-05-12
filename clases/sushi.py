from clases import alimentos
class Sushi(Alimentos):
    def __init__(self, nombre, precio, tipo_sushi):
        super().__init__(nombre, precio)
        self.tipo_sushi = tipo_sushi

    def descripcion(self):
        print(f"El sushi {self.nombre} es de tipo {self.tipo_sushi}. Su precio es {self.precio}.")