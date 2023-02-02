result = input().strip()
answer = input().strip()

score = 0

if len(result) != len(answer):
    print("Incomplete answer")
else:
    for i in range(len(answer)):
        if answer[i] == result[i]:
            score += 1
    print(score)