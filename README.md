# moneyline
Convert between American, decimal, and fractional odds

```
as_american(2.2)    -> "+120"
as_american("6/5")  -> "+120"

as_decimal("+120")  -> 2.2
as_decimal("6/5") -> 2.2

as_fraction("+120") -> "6/5"
as_fraction(2.2)   -> "6/5"
```

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
