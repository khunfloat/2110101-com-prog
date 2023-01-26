d, m, y = int(input()), int(input()), int(input())-543

pass_day = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

doy = d + pass_day[m]

if ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)) and m > 2:
    doy += 1

print(doy)