a, b, c = float(input()), float(input()), float(input())

from math import sqrt

res_1 = round((-b - sqrt(b**2 - (4 * a * c))) / (2 * a), 3)
res_2 = round((-b + sqrt(b**2 - (4 * a * c))) / (2 * a), 3)

print(res_1, res_2)