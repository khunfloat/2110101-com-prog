from math import dist

data, dists = [], []

for i in range(int(input())):
    x, y = [float(e) for e in input().strip().split()]
    data.append((x, y))

    d = dist((0, 0), (x, y))

    dists.append([d, i+1, (x, y)])

_, i, p = sorted(dists)[-2]

print('#'+str(i)+': '+str(p))