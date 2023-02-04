data = [int(e) for e in input().strip().split(' ')]
res = []

for e in data:
    if e not in res:
        res.append(e)

print(len(res))
print(sorted(res)[:10])