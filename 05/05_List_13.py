res = []

indexer = True

def index(bool):
    if bool: return -1
    else: return 0

for i in range(int(input())):
    res.insert(index(indexer), int(input()))
    indexer = not bool

set_2 = input().strip()
if set_2 != '':
    set_2 = [int(e) for e in set_2.strip().split(' ')]

for n in set_2:
    res.insert(index(indexer), int(input()))
    indexer = not bool

while True:

    n = int(input())
    if n != -1:
        res.insert(index(indexer), int(input()))
        indexer = not bool
    else:
        break

print(res)   