import unittest
import numpy as np
from scipy import integrate as integrate
import sys
sys.path.append('../')
from gauss_jordan import gauss_jordan

class Test_simp(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @staticmethod
    def A_1():
        return np.array(([1, 2, 1, 1]
                         , [2, 1, 1, 2]
                         , [1, 1, 2, 3]))
    
    @staticmethod
    def A_2():
        return np.array(([1, 1, 3, 5]
                         , [1, 3, 1, 5]
                         , [3, 1, 1, 5]))

    def test_linearsolve(self):
        for mat in (self.A_1(), self.A_2()):
            res = gauss_jordan(mat)
            np.testing.assert_array_almost_equal(mat[:, :-1] @ res, mat[:, -1])

if __name__ == '__main__':
    unittest.main()