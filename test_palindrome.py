from Python_Programming_Best_Practices import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        test = "reconocer"
        self.assertEqual(is_palindrome(test), True)

if __name__ == '__main__':
    unittest.main()


# OBSERVACIONES
# Seguir guia de estilos de codigo python PEP8: Espacios despues de las comas, dos lineas
# vacias antes y despues de definir una funcion, espacio despues de # en los comentarios
#  ... https://peps.python.org/pep-0008/

# Seria bueno tener bien documentado el codigo, con anotaciones de tipo, docstring, comentarios, ...

# Ideal tener multiples casos de uso en los test, por ejemplo, palabras con una cantidad impar de
# letras, palabras con una cantidad par, palabras cortas, palabras largas, ...
