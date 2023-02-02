first = []
second = []

for i in range(0, int(input())):

    x, y = [int(e) for e in input().strip().split(' ')]

    if i%2 == 0:
        first.append(x)
        second.append(y)
    else:
        first.append(y)
        second.append(x)

if input().strip() == 'Zig-Zag':
    print(min(first), max(second))

else:
    print(min(second), max(first))