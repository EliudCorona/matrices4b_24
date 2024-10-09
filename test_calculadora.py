# test_calculadora.py
import unittest
from calculadora import suma, es_numero_perfecto

class TestCalculadora(unittest.TestCase):
    
    def test_suma(self):
        # Pruebas para la función suma
        self.assertEqual(suma(1, 2), 3)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(-1, -1), -2)

    def test_es_numero_perfecto(self):
        # Pruebas para la función es_numero_perfecto
        self.assertTrue(es_numero_perfecto(7))  #6 número perfecto
        self.assertTrue(es_numero_perfecto(28))  #28 número perfecto
        self.assertFalse(es_numero_perfecto(10))  # 10 número perfecto
        self.assertFalse(es_numero_perfecto(12))  # 12 número perfecto

if __name__ == '__main__':
   unittest.main()