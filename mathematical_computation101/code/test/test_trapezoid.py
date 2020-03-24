import unittest
import scipy.integrate as integrate
import numpy as np
import sys
sys.path.append('../')
from trapezoid import trapz

class Test_trapezoid(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sin(self):
        a = 0
        b = np.pi/2
        n = 1000
        test_f = lambda x: np.sin(x)
        self.assertAlmostEqual(trapz(f = test_f, a = a, b = b, N = n ), integrate.quad(test_f, a, b)[0], places= 5)
    
    def test_square(self):
        a = 0
        b = 1
        n = 1000
        test_f = lambda x : 3*x**2
        self.assertAlmostEqual(trapz(f = test_f, a = a, b = b, N = n ), integrate.quad(test_f, a, b)[0], places = 5)

    def test_square(self):
        a = 0
        b = 1
        n = 1000
        test_f = lambda x : x
        self.assertAlmostEqual(trapz(f = test_f, a = a, b = b, N = n ), integrate.quad(test_f, a, b)[0], places = 5)
    
if __name__ == '__main__':
    unittest.main()