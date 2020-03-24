import unittest
from numpy import vectorize, arange
import sys
sys.path.append('../')
from binary_to_decimal import binary_to_decimal_1, binary_to_decimal_2 

class Test_binary_decimal(unittest.TestCase):
    def setUp(self):
        x = list(arange(0, 10000))
        self.data = list(map(lambda a: bin(a)[2:] , x))
        self.answer = x


    def tearDown(self):
        self.data
        self.answer

    def test_binary_to_decimal_1(self):
        binary_to_decimal_vec_1 = vectorize(binary_to_decimal_1)
        self.assertEqual(list(binary_to_decimal_vec_1(self.data)), self.answer)
    
    def test_binary_to_decimal_2(self):
        binary_to_decimal_vec_2 = vectorize(binary_to_decimal_2)
        self.assertEqual(list(binary_to_decimal_vec_2(self.data)), self.answer)

if __name__ == '__main__':
    unittest.main()

