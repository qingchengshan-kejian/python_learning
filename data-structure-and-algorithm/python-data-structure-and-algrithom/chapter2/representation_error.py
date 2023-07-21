# print(1-0.9)
# print(1-0.9 == 0.1)

import decimal
x = decimal.Decimal(3.14)
y = decimal.Decimal(2.74)
print(x * y)

decimal.getcontext().prec = 4
print(x * y)


import fractions
print(fractions.Fraction(3, 4))
print(fractions.Fraction(0.5))
print(fractions.Fraction(".25"))
