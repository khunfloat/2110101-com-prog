n = int(input())
res = [str(n)]
while n != 1: 
    if n%2 == 0: 
        n = int(n / 2)
    else: 
        n = int(3*n + 1 )

    res.append(str(n))

print('->'.join(res[-15:]))