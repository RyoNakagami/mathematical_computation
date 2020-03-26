import unittest
import numpy as np
from scipy import integrate as integrate
import sys
sys.path.append('../')
from simp import simp


class Test_simp(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sin(self):
        a = 0
        b = np.pi/2
        n = 1000
        test_f = lambda x: np.sin(x)
        scipy_x = np.linspace(a, b, n+1)
        scipy_y = test_f(scipy_x)
        self.assertAlmostEqual(simp(f = test_f, a = a, b = b, N = n ), integrate.simps(scipy_y, scipy_x), places= 9)
    
    def test_square(self):
        a = 0
        b = 1
        n = 1000
        test_f = lambda x: np.square(x)
        scipy_x = np.linspace(a, b, n+1)
        scipy_y = test_f(scipy_x)
        self.assertAlmostEqual(simp(f = test_f, a = a, b = b, N = n), integrate.simps(scipy_y, scipy_x), places = 9)

    def test_linear(self):
        a = 0
        b = 1
        n = 1000
        test_f = lambda x : x
        scipy_x = np.linspace(a, b, n+1)
        scipy_y = test_f(scipy_x)
        self.assertAlmostEqual(simp(f = test_f, a = a, b = b, N = n ), integrate.simps(scipy_y, scipy_x), places = 9)
    
if __name__ == '__main__':
    unittest.main()