res = []

ind = True #หลัง

for i in range(int(input())):
    e = int(input())
    if ind:
        res.append(e)
    else:
        res.insert(0, e)

    ind = not ind

set2 = input()

if set2 != '':
    set2 = [int(e) for e in set2.split(' ')]

    for e in set2:
        if ind:
            res.append(e)
        else:
            res.insert(0, e)

        ind = not ind

while True:
    e = int(input().strip())

    if e == -1:
        break
    else:
        if ind:
            res.append(e)
        else:
            res.insert(0, e)

        ind = not ind


print(res)