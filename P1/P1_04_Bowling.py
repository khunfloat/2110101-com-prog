game = input()
frame = int(input())

result = []

for i in range(0, 9):
    if game[0] == 'X':
        if game[2] == '/':
            slash = 10-int(game[1])
            if slash == 10: slash = 'X'
            result.append(game[0]+game[1]+str(slash))
        else:
            result.append(game[0]+game[1]+game[2])
        game = game[1:]
    else:
        if game[1] == '/':
            slash = 10-int(game[0])
            if slash == 10: slash = 'X'
            result.append(game[0]+str(slash)+game[2])
        else:
            result.append(game[0]+game[1])
        game = game[2:]

# last frame
if game[1] == '/':
    slash = 10-int(game[0])
    if slash == 10: slash = 'X'
    game = game[0]+str(slash)+game[2]
if len(game) == 3:
    if game[2] == '/':
        slash = 10-int(game[1])
        if slash == 10: slash = 'X'
        game = game[0]+game[1]+str(slash)

result.append(game)

# main
if frame in range(1, 11):

    sum_score = 0

    for score in result[frame-1]:
        if score == 'X':
            sum_score += 10
        else:
            sum_score += int(score)
    
    print(sum_score)

else:

    sum_score = 0

    for frame in result:
        for score in frame:
            if score == 'X':
                sum_score += 10
            else:
                sum_score += int(score)
        
    print(sum_score)