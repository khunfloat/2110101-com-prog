a = float(input())

L, U = 0, a
x = (L + U) / 2

while not (abs(a - 10**x) <= (10**(-10))*max(a, 10**x)):
    if 10**x > a:
        L, U = L, x
    elif 10**x < a:
        L, U = x, U
    x = (L + U) / 2

print(round(x, 6))