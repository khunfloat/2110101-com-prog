sum_par = 0
sum_stroke = 0
sum_fixed = 0

for _ in range(0, 9):
    par, stroke, choose = [int(e) for e in input().strip().split(' ')]

    if choose == 1:
        sum_par += par
        sum_stroke += stroke
        sum_fixed += min(par+2, stroke)
    else:
        sum_par += par
        sum_stroke += stroke

handicap = int((0.8 * (1.5 * sum_fixed - sum_par)) // 1)

print(sum_stroke)
print(handicap)
print(sum_stroke - handicap)