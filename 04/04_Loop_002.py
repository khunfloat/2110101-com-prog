d = [int(e) for e in input().strip().split(' ')]
p = d[-1]
i, j = -1, 0
n = len(d)

while j < n-1:
    if d[j] <= p:
        i += 1
        d[i], d[j] = d[j], d[i]
    j += 1

d[i+1], d[-1] = d[-1], d[i+1]

print(d)
