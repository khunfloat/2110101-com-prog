first_max = -99999
first_min = 99999
second_max = -99999
second_min = 99999

count = 0

while True:

    a = input()

    if 'Zig' in a:
        break

    x, y = [int(e) for e in a.strip().split(' ')]

    if count%2 == 0:
        first_max = max(first_max, x)
        first_min = min(first_min, x)
        second_max = max(second_max, y)
        second_min = min(second_min, y)
    else:
        first_max = max(first_max, y)
        first_min = min(first_min, y)
        second_max = max(second_max, x)
        second_min = min(second_min, x)

    count += 1

if a == 'Zig-Zag':
    print(first_min, second_max)

else:
    print(second_min, first_max)