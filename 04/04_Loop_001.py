k, t = 1, 1
p = float(input())

while True:
    
    t = (t*(365 - (k-1))) / 365

    if 1-t >= p:
        print(k)
        break
    else:
        k += 1