from ..moneyline import *
import unittest

odds = {
    "f200": ("-200", 1.5, "1/2"),
    "f190": ("-190", 1.526, "263/500"),
    "f180": ("-180", 1.556, "139/250"),
    "f170": ("-170", 1.588, "147/250"),
    "f160": ("-160", 1.625, "5/8"),
    "f150": ("-150", 1.667, "667/1000"),
    "f140": ("-140", 1.714, "357/500"),
    "f130": ("-130", 1.769, "769/1000"),
    "f120": ("-120", 1.833, "833/1000"),
    "f110": ("-110", 1.909, "909/1000"),
    "f105": ("-105", 1.952, "119/125"),
    
    "u100": ("+100", 2.0, "1/1"),
    "u105": ("+105", 2.05, "21/20"),
    "u110": ("+110", 2.1, "11/10"),
    "u115": ("+115", 2.15, "23/20"),
    "u120": ("+120", 2.2, "6/5"),
    "u130": ("+130", 2.3, "13/10"),
    "u140": ("+140", 2.4, "7/5"),
    "u150": ("+150", 2.5, "3/2"),
    "u160": ("+160", 2.6, "8/5"),
    "u170": ("+170", 2.7, "17/10"),
    "u180": ("+180", 2.8, "9/5"),
    "u190": ("+190", 2.9, "19/10"),
    "u200": ("+200", 3.0, "2/1"),
    "u300": ("+300", 4.0, "3/1")
}
        

class TestMoneyline(unittest.TestCase):    

    def setUp(self):
        self.o1 = 1.10
        self.o2 = "+150"
        self.o3 = "-110"
        self.o4 = "200/100"
        

    def test_is_fractional(self):
        result1 = is_fractional(odds["f110"][0])
        result2 = is_fractional(odds["f110"][1])
        result3 = is_fractional(odds["u110"][1])
        result4 = is_fractional(odds["f110"][2])
        result5 = is_fractional(None)
        result6 = is_fractional("")

        self.assertEqual(result1, False)
        self.assertEqual(result2, False)
        self.assertEqual(result3, False)
        self.assertEqual(result4, True)
        self.assertEqual(result5, False)
        self.assertEqual(result6, False)

    def test_is_american(self):
        result1 = is_american(odds["f110"][0])
        result2 = is_american(odds["f110"][1])
        result3 = is_american(odds["u110"][1])
        result4 = is_american(odds["f110"][2])
        result5 = is_american(None)
        result6 = is_american("")

        self.assertEqual(result1, False)
        self.assertEqual(result2), True)
        self.assertEqual(result3, True)
        self.assertEqual(result4, False)
        self.assertEqual(result5, False)
        self.assertEqual(result6, False)

    def test_is_decimal(self):
        result1 = is_decimal(odds["f110"][0])
        result2 = is_decimal(odds["f110"][1])
        result3 = is_decimal(odds["u110"][1])
        result4 = is_decimal(odds["f110"][2])
        result5 = is_decimal(None)
        result6 = is_decimal("")

        self.assertEqual(result1, True)
        self.assertEqual(result2, False)
        self.assertEqual(result3, False)
        self.assertEqual(result4, False)
        self.assertEqual(result5, False)
        self.assertEqual(result6, False)


    def test_as_american(self):
        for key in odds.keys():
            # american > american
            self.assertEqual(as_american(odds[key][0]), odds[key][0]) 
            
            # decimal > american
            self.assertEqual(as_american(odds[key][1]), odds[key][0]) 

            # fraction > american
            self.assertEqual(as_american(odds[key][2]), odds[key][0])
       
        with self.assertRaises(ValueError):
            as_american(None)

        with self.assertRaises(ValueError):
            as_american("")

    def test_as_decimal(self):
        for key in odds.keys():
            # american > decimal
            self.assertEqual(as_decimal(odds[key][0]), odds[key][1]) 
            
            # decimal > decimal
            self.assertEqual(as_decimal(odds[key][1]), odds[key][1]) 

            # fraction > decimal
            self.assertEqual(as_decimal(odds[key][2]), odds[key][1]) 

        with self.assertRaises(ValueError):
            as_decimal(None)
        with self.assertRaises(ValueError):
            as_decimal("")

    def test_as_fraction(self):
        for key in odds.keys():
            # american > fraction
            self.assertEqual(as_fraction(odds[key][0]), odds[key][2]) 
            
            # decimal > fraction
            self.assertEqual(as_fraction(odds[key][1]), odds[key][2]) 

            # fraction > fraction
            self.assertEqual(as_fraction(odds[key][2]), odds[key][2]) 

        with self.assertRaises(ValueError):
            as_fraction(None)
        with self.assertRaises(ValueError):
            as_fraction("")

if __name__ == "__main__":
    unittest.main()