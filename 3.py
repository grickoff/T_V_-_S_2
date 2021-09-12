import math

p = 0.5
n = 144
m = 70

Pm = (((n * p) ** m) / math.factorial(m)) * math.exp(-(n * p))

print(Pm)
#получил ответ: 0.046309172162262796
