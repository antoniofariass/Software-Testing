import unittest
from qual_triangulo import Triangulo

class triangulo_test(unittest.TestCase):
    
    def setUp(self):
        self.triangulo = Triangulo()

    def test_triangulo_invalido(self):
        self.assertTrue(self.triangulo.invalido(1,2,3))

    def test_triangulo_invalido_limite_a(self):
        self.assertTrue(self.triangulo.invalido(10000000,1,1))

    def test_triangulo_invalido_limite_b(self):
        self.assertTrue(self.triangulo.invalido(1,10000000,1))  

    def test_triangulo_invalido_limite_c(self):
        self.assertTrue(self.triangulo.invalido(1,1,10000000))
    
    def test_triangulo_invalido_limite_zero_a(self):
        self.assertTrue(self.triangulo.invalido(0,1,1))

    def test_triangulo_invalido_limite_zero_b(self):
        self.assertTrue(self.triangulo.invalido(1,0,1))
    
    def test_triangulo_invalido_limite_zero_c(self):
        self.assertTrue(self.triangulo.invalido(1,1,0))
    
    def test_triangulo_valido(self):
        self.assertFalse(self.triangulo.invalido(2,2,3))

    def test_triangulo_valido_isosceles_nao_retangulo(self):
        self.assertFalse(self.triangulo.invalido(4,3,3))
        self.assertEqual(self.triangulo.tipo(4,3,3), "Isosceles")
        self.assertFalse(self.triangulo.retangulo(4,3,3))
    
    def test_triangulo_valido_escaleno_retangulo(self):
        self.assertFalse(self.triangulo.invalido(3,4,5))
        self.assertEqual(self.triangulo.tipo(3,4,5), "Escaleno")
        self.assertTrue(self.triangulo.retangulo(3,4,5))

    def test_triangulo_valido_escaleno_nao_retangulo(self):
        self.assertFalse(self.triangulo.invalido(7,8,10))
        self.assertEqual(self.triangulo.tipo(7,8,10), "Escaleno")
        self.assertFalse(self.triangulo.retangulo(7,8,10))
    
    def test_triangulo_valido_equilatero_nao_retangulo(self):
        self.assertFalse(self.triangulo.invalido(6,6,6))
        self.assertEqual(self.triangulo.tipo(6,6,6), "Equilatero")
        self.assertFalse(self.triangulo.retangulo(6,6,6))
   
if __name__ == "__main__":
   unittest.main()

