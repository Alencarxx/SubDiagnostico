# test_calculadora.py
import unittest
from calculadora import calcular_consumo_energia

class TestCalculoConsumoEnergia(unittest.TestCase):
    def test_calculo_consumo(self):
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
        self.assertEqual(calcular_consumo_energia(numeros_binarios), 198)

if __name__ == '__main__':
    unittest.main()
