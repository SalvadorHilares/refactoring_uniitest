import unittest

import app

import app_refactorizada


class TestUtils(unittest.TestCase):
    def test_app(self):
        test = app.CalculaGanador()
        self.assertIsInstance(test.leerdatos(), list) # Valida que se haya leido un array
        self.assertTrue(len(test.leerdatos()) != 0) # Valida que se hayan leidos los datos del .csv
        result = test.calcularganador(test.leerdatos())
        self.assertTrue(result[0] == 'Dennis Reyna') # Ganador de las elecciones en el archivo .csv actual
        self.assertTrue(len(result) == 1) # Valida que solo se haya retornado un ganador
    
    def test_app_refactorizada(self):
        test = app.CalculaGanador()
        self.assertIsInstance(test.leerdatos(), list) # Valida que se haya leido un array
        self.assertTrue(len(test.leerdatos()) != 0) # Valida que se hayan leidos los datos del .csv
        result = test.calcularganador(test.leerdatos())
        self.assertTrue(result[0] == 'Dennis Reyna') # Ganador de las elecciones en el archivo .csv actual
        self.assertTrue(len(result) == 1) # Valida que solo se haya retornado un ganador


if __name__ == '__main__':
    unittest.main()