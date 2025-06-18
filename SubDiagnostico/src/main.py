# main.py
from calculadora import calcular_consumo_energia

def main():
    numeros_binarios = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]
    resultado = calcular_consumo_energia(numeros_binarios)
    print(f'O consumo de energia do submarino é: {resultado}')

if __name__ == "__main__":
    main()
