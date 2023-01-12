a, b, c = int(input()), int(input()), int(input())

from math import sqrt

pos_res = (-b + sqrt(b**2 - (4 * a * c))) / (2 * a)
neg_res = (-b - sqrt(b**2 - (4 * a * c))) / (2 * a)

print(pos_res)
print(neg_res)