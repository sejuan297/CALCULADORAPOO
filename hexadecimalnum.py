# Clase Hexadecimalnum
from numero import Numero

class HexadecimalNum(Numero):
    def validar(self) -> bool:
        try:
            int(self.valor, 16)
            return True
        except ValueError:
            return False

    def convertir_a_decimal(self) -> int:
        return int(self.valor, 16)

    @classmethod
    def desde_decimal(cls, valor: int):
        return cls(hex(valor)[2:].upper()) 

    def __str__(self):
        return f"{self.valor} (Hexadecimal)"
