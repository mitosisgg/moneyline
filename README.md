# moneyline
Convert between American, decimal, and fractional odds

as_american(2.0)    -> "+100"
as_american("1/1")  -> "+100"

as_decimal("+120")  -> 2.05
as_decimal("21/20") -> 2.05

as_fraction("+120") -> "21/20"
as_fraction(2.15)   -> "23/20"


| American odds | Decimal   | Fractional|
| :---          | :---      | :---      |
| -190          | 1.526     | 263/500   |
| -180          | 1.556     | 139/250   |
| -170          | 1.588     | 147/250   |
| -160          | 1.625     | 5/8       |
|  ...          | ...       | ...       |
| +100          | 2.0       | 1/1       |
| +120          | 2.05      | 21/20     |
| +130          | 2.1       | 11/10     |
| +140          | 2.15      | 23/20     |



