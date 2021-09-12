import math

p = 0.8
n = 100
m = 85

Pm = (((n * p) ** m) / math.factorial(m)) * math.exp(-(n * p))

print(Pm)
#получил ответ: 0.03709261434369179