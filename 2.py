import math

p = 0.0004
n = 5000
m1 = 0
m2 = 2

Pm1 = (((n * p) ** m1) / math.factorial(m1)) * math.exp(-(n * p))
Pm2 = (((n * p) ** m2) / math.factorial(m2)) * math.exp(-(n * p))

print(Pm1, Pm2)
#получил ответы:
#   ни одна = 0.1353352832366127
#   ровно две лампочки = 0.2706705664732254
