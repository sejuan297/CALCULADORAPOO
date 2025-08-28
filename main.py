# Menu principal 
from decimalnum import DecimalNum
from binarionum import BinarioNum
from octalnum import OctalNum
from hexadecimalnum import HexadecimalNum
from romanonum import RomanoNum

TIPOS = {
    "decimal": DecimalNum,
    "binario": BinarioNum,
    "octal": OctalNum,
    "hexadecimal": HexadecimalNum,
    "romano": RomanoNum
}

def crear_numero(tipo: str, valor: str):
    clase = TIPOS[tipo.lower()]
    num = clase(valor)
    if not num.validar():
        raise ValueError(f"{valor} no es un número válido en {tipo}")
    return num

def menu():
    print("=== Calculadora Numérica Universal ===")
    print("Tipos disponibles: decimal, binario, octal, hexadecimal, romano")

    tipo1 = input("Ingrese el tipo del primer número: ")
    valor1 = input("Ingrese el valor: ")
    num1 = crear_numero(tipo1, valor1)

    tipo2 = input("Ingrese el tipo del segundo número: ")
    valor2 = input("Ingrese el valor: ")
    num2 = crear_numero(tipo2, valor2)

    print("\nOperaciones disponibles: suma y resta")
    op = input("Seleccione operación: ")

    dec1 = num1.convertir_a_decimal()
    dec2 = num2.convertir_a_decimal()

    if op == "suma":
        resultado = dec1 + dec2
    elif op == "resta":
        resultado = dec1 - dec2
    else:
        print("Operación no válida.")
        return

    tipo_res = input("¿En qué tipo quiere ver el resultado? ")
    clase_res = TIPOS[tipo_res.lower()]
    num_res = clase_res.desde_decimal(resultado)

    print(f"\nResultado: {num_res}")

if __name__ == "__main__":
    menu()
