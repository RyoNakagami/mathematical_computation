import unittest
from numpy import vectorize, arange
import sys
sys.path.append('../')
from decimal_to_binary import *

class Test_decimal_to_binary(unittest.TestCase):
    def setUp(self):
        x = list(arange(0, 10000))
        self.data = x
        self.answer = list(map(lambda a: bin(a)[2:], x))

    def tearDown(self):
        self.data
        self.answer

    def test_unittest_decimal_to_binary(self):
        decimal_to_binary_vec = vectorize(decimal_to_binary)
        self.assertEqual(list(decimal_to_binary_vec(self.data)), self.answer)

if __name__ == '__main__':
    unittest.main()
