# Clase Decimalnum
from numero import Numero

class DecimalNum(Numero):
    def validar(self) -> bool:
        return self.valor.isdigit()

    def convertir_a_decimal(self) -> int:
        return int(self.valor)

    @classmethod
    def desde_decimal(cls, valor: int):
        return cls(str(valor))

    def __str__(self):
        return f"{self.valor} (Decimal)"
