from math import log10

a, b, c, d = [int(e) for e in input().split()]

if a == 1:
    c, d = d, c
    if b == 1:
        c += d
    elif b == 2:
        c -= d
    elif b != 3:
        c += c**d
    else:
        c /= d

    a = (d + ((c / b)**3 + d)**0.5) / (2 + b*d)

else:
    if a == 2:
        if b > 1:
            c += d
        if b > 2:
            c /= d
        if b > 3:
            c += c**d
        else:
            a = log10(c)
    else:
        while a > d:
            a -= 2
            if a < b:
                break
            else:
                c += a

print(a, b, c, d)