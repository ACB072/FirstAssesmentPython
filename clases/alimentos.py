from abc import ABC, abstractmethod

class Alimentos(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    @abstractmethod
    def descripcion(self):
        pass