# Clase Romanonum
from numero import Numero

class RomanoNum(Numero):
    simbolos = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400,
        "C": 100, "XC": 90, "L": 50, "XL": 40,
        "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
    }

    def validar(self) -> bool:
        try:
            self.convertir_a_decimal()
            return True
        except:
            return False

    def convertir_a_decimal(self) -> int:
        i = 0
        num = 0
        while i < len(self.valor):
            if i+1 < len(self.valor) and self.valor[i:i+2] in self.simbolos:
                num += self.simbolos[self.valor[i:i+2]]
                i += 2
            else:
                num += self.simbolos[self.valor[i]]
                i += 1
        return num

    @classmethod
    def desde_decimal(cls, valor: int):
        res = ""
        for simbolo, val in cls.simbolos.items():
            while valor >= val:
                res += simbolo
                valor -= val
        return cls(res)

    def __str__(self):
        return f"{self.valor} (Romano)"
