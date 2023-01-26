score = [float(sc) for sc in input().split(' ')]

max_sc = 0
min_sc = 0

if score[0] > score[1]:
    max_sc = score[0]
    min_sc = score[1]
else:
    max_sc = score[1]
    min_sc = score[0]

if score[2] > max_sc:
    max_sc = score[2]
elif score[2] < min_sc:
    min_sc = score[2]

if score[3] > max_sc:
    max_sc = score[3]
elif score[3] < min_sc:
    min_sc = score[3]

score.remove(max_sc)
score.remove(min_sc)

print(round((score[0] + score[1])/2, 2))