from fractions import Fraction
from decimal import Decimal

def as_american(odds):
    if is_decimal(odds):
        if odds >= 2.0:
            return "+" + str(round((odds - 1) * 100))
        elif 1.01 <= odds <= 1.99:
            return str(round(-100 / (odds - 1)))
    elif is_fractional(odds):
        f = Fraction(odds)
        decimal = f.numerator / f.denominator
        if decimal >= 1:
            return "+" + str(round(decimal * 100))
        else:
            return str(round(-100 / decimal))
    elif is_american(odds):
        return odds
    else:
        raise ValueError("Can't convert {o} to american odds".format(o=odds))

def as_decimal(odds):
    if is_decimal(odds):
        return odds
    elif is_fractional(odds):
        f = Fraction(odds)
        return round((f.numerator / f.denominator) + 1, 3)
    elif is_american(odds):
        if isinstance(odds, str) and len(odds) > 1:
            sign = odds[0]
            odds = int(odds[1:])
            if sign == "+":
                odds = (odds / 100) + 1
                return round(odds, 3)
            elif sign == "-":
                odds = (100 / odds) + 1
                return round(odds, 3)
        else: 
            raise()
    else:
        raise ValueError("Can't convert {o} to decimal odds".format(o=odds))

def as_fraction(odds):
    if is_decimal(odds):
        if odds.is_integer():
            numerator = int(odds) -1
            return f"{numerator}/1" 
        else:
            f = Fraction(Decimal(str(odds)))
            odds = f - 1
            return str(odds)
    elif is_fractional(odds):
        return odds
    elif is_american(odds):
        if odds == "+100":
            return "1/1"
        decimal = as_decimal(odds)
        return as_fraction(decimal)
        
    else:
        raise ValueError("Can't convert {o} to fractional odds".format(o=odds))

def is_decimal(odds):
    return isinstance(odds, float) or isinstance(odds, int)

def is_american(odds):
    if isinstance(odds, str) and odds.strip():    
        try:
            sign = odds.strip()[0]
            odds = odds.strip()[1:]
            odds = int(odds)
            if sign in ["+", "-"] and isinstance(odds, int):
                return True
        except:
            print('Could not convert odds {o} to int'.format(o=odds))
    return False

def is_fractional(odds):
    try:
        if odds == "1" or odds == 1:
            return True
        if isinstance(odds, str) and odds.find('/') != -1:
            Fraction(odds)
            return True
        return False
    except:
        print('is not fractional')
        return False
        

        