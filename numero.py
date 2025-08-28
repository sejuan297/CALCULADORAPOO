# numero.py
from abc import ABC, abstractmethod
# No usa encapsulamiento 
class Numero(ABC):
    def __init__(self, valor: str):
        self.valor = valor 

    @abstractmethod
    def validar(self) -> bool:
        """Validar si el valor corresponde a la base o formato"""
        pass

    @abstractmethod
    def convertir_a_decimal(self) -> int:
        """Convertir el valor a decimal"""
        pass

    @abstractmethod
    def desde_decimal(cls, valor: int):
        """Crear un número desde decimal"""
        pass

    @abstractmethod
    def __str__(self):
        """Mostrar el número como string"""
        pass
