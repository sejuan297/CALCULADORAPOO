# Clase Binarionum
from numero import Numero

class BinarioNum(Numero):
    def validar(self) -> bool:
        return all(c in "01" for c in self.valor)

    def convertir_a_decimal(self) -> int:
        return int(self.valor, 2)

    @classmethod
    def desde_decimal(cls, valor: int):
        return cls(bin(valor)[2:])  
    
    def __str__(self):
        return f"{self.valor} (Binario)"
