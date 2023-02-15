data, dists = [], []

for i in range(int(input())):
    x, y = [float(e) for e in input().strip().split()]
    data.append((x, y))

    d = (x**2+y**2)**(1/2)

    dists.insert(0, [d, i+1, (x, y)])

_, i, p = sorted(dists)[2]

print("#{}: {}".format(i, p))