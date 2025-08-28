# Clase Octalnum
from numero import Numero

class OctalNum(Numero):
    def validar(self) -> bool:
        return all(c in "01234567" for c in self.valor)

    def convertir_a_decimal(self) -> int:
        return int(self.valor, 8)

    @classmethod
    def desde_decimal(cls, valor: int):
        return cls(oct(valor)[2:])  

    def __str__(self):
        return f"{self.valor} (Octal)"
