from ..moneyline import *
import unittest

class TestMoneyline(unittest.TestCase):    

    def setUp(self):
        self.o1 = 1.10
        self.o2 = "+150"
        self.o3 = "-110"
        self.o4 = "200/100"
        self.o5 = None
        self.o6 = ""

    def test_is_fractional(self):
        result1 = is_fractional(self.o1)
        result2 = is_fractional(self.o2)
        result3 = is_fractional(self.o3)
        result4 = is_fractional(self.o4)
        result5 = is_fractional(self.o5)
        result6 = is_fractional(self.o6)

        self.assertEqual(result1, False)
        self.assertEqual(result2, False)
        self.assertEqual(result3, False)
        self.assertEqual(result4, True)
        self.assertEqual(result5, False)
        self.assertEqual(result6, False)

    def test_is_american(self):
        result1 = is_american(self.o1)
        result2 = is_american(self.o2)
        result3 = is_american(self.o3)
        result4 = is_american(self.o4)
        result5 = is_american(self.o5)
        result6 = is_american(self.o6)

        self.assertEqual(result1, False)
        self.assertEqual(result2, True)
        self.assertEqual(result3, True)
        self.assertEqual(result4, False)
        self.assertEqual(result5, False)
        self.assertEqual(result6, False)

    def test_is_decimal(self):
        result1 = is_decimal(self.o1)
        result2 = is_decimal(self.o2)
        result3 = is_decimal(self.o3)
        result4 = is_decimal(self.o4)
        result5 = is_decimal(self.o5)
        result6 = is_decimal(self.o6)

        self.assertEqual(result1, True)
        self.assertEqual(result2, False)
        self.assertEqual(result3, False)
        self.assertEqual(result4, False)
        self.assertEqual(result5, False)
        self.assertEqual(result6, False)


    def test_as_american(self):
        result1 = as_american(self.o1)
        result2 = as_american(self.o2)
        result3 = as_american(self.o3)
        result4 = as_american(self.o4)

        self.assertEqual(result1, "-1000")
        self.assertEqual(result2, "+150")
        self.assertEqual(result3, "-110")
        self.assertEqual(result4, "+200")
       
        with self.assertRaises(ValueError):
            as_american(self.o5)

        with self.assertRaises(ValueError):
            as_american(self.o6)

    def test_as_decimal(self):
        result1 = as_decimal(self.o1)
        result2 = as_decimal(self.o2)
        result3 = as_decimal(self.o3)
        result4 = as_decimal(self.o4)

        self.assertEqual(result1, 1.10)
        self.assertEqual(result2, 2.5)
        self.assertEqual(result3, 1.91)
        self.assertEqual(result4, 3.0)
        
        with self.assertRaises(ValueError):
            as_decimal(self.o5)
        with self.assertRaises(ValueError):
            as_decimal(self.o6)

    def test_as_fraction(self):
        result1 = as_fraction(self.o1)
        result2 = as_fraction(self.o2)
        result3 = as_fraction(self.o3)
        result4 = as_fraction(self.o4)

        self.assertEqual(result1, "1/10")
        self.assertEqual(result2, "3/2")
        self.assertEqual(result3, "91/100")
        self.assertEqual(result4, "200/100")

        with self.assertRaises(ValueError):
            as_fraction(self.o5)
        with self.assertRaises(ValueError):
            as_fraction(self.o6)

if __name__ == "__main__":
    unittest.main()