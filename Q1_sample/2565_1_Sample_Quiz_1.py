el = [int(e) for e in input().split()] + [' ']
k = int(input())

response = 0
n = 1

for i in range(len(el)):
    if el[i] == ' ':
        break
    else:
        if el[i] == el[i+1]:
            n = n + 1
        elif el[i] != el[i+1]:
            if n < k:
                response += n * el[i]
            n = 1

print(response)