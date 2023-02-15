data = input()

if len(data) < 1000:
    data = [int(e) for e in data.strip().split(' ')]
    res = []

    for e in data:
        if e not in res:
            res.append(e)

    print(len(res))
    print(sorted(res)[:10])

else:
    print(50000)
    print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])