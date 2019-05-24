import unittest
from dollar import Dollar


class DollarTest(unittest.TestCase):
    # TODO $5 + 10CHF = $10(レートが2:1の場合)
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        # TODO nullとの等価性比較
        # TODO 他のオブジェクトとの等価性比較
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))

