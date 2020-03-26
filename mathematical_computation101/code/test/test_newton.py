import unittest
import numpy as np
from scipy import integrate as integrate
import sys
sys.path.append('../')
from newton_method import newton_method

class Test_simp(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @staticmethod
    def f1(x):
        return x**2 - 2*x - 1  # == (x-1)**2 - 2

    @staticmethod
    def f1_1(x):
        return 2*x - 2

    @staticmethod
    def f2(x):
        return np.exp(x) - np.cos(x)

    @staticmethod
    def f2_1(x):
        return np.exp(x) + np.sin(x)

    def test_newton(self):
        for f, f_1 in [(self.f1, self.f1_1),
                       (self.f2, self.f2_1)]:
            x = newton_method(f = f, f_foc = f_1, initial = 3)
            self.assertAlmostEqual(f(x), 0, places = 7)

if __name__ == '__main__':
    unittest.main()


