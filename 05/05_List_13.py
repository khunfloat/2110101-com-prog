res = []

for i in range(int(input())):
    if i%2 == 0:
        res.append(int(input()))
    else:
        res.insert(0, int(input()))

len_set_1 = len(res)

set_2 = input().strip()
if set_2 != '':
    set_2 = [int(e) for e in set_2.strip().split(' ')]

for i, n in enumerate(set_2):
    i += len_set_1
    if i%2 == 0:
        res.append(n)
    else:
      res.insert(0, n)

len_set_2 = len(res)

while (n := int(input())) != -1:
    if len_set_2%2 == 0:
        res.append(n)
    else:
      res.insert(0, n)
    len_set_2 += 1

print(res)   