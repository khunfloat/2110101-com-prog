m = int(input())

mapper = {
    "R R": (0, 0),
    "R P": (0, 1),
    "R S": (1, 0),
    "P R": (1, 0),
    "P P": (0, 0),
    "P S": (0, 1),
    "S R": (0, 1),
    "S P": (1, 0),
    "S S": (0, 0)
}

player_1_score = 0
player_2_score = 0

count = 0

while True:
    p1, p2 = mapper[input()]

    count += 1

    player_1_score, player_2_score = player_1_score + p1, player_2_score + p2

    if player_1_score == m or player_2_score == m:
        break
    elif count == (3 * m):
        break

print(str(player_1_score) + ' ' + str(player_2_score))

if player_1_score > player_2_score:
    print('Player 1 wins')
elif player_2_score > player_1_score:
    print('Player 2 wins')
else:
    print('Tie')