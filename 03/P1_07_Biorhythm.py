from math import pi, sin

def day_of_year(d, m, y):
    pass_day = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    doy = d + pass_day[m]
    if ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)) and m > 2:
        doy += 1
    return doy

def red_zone_day(d, m, y):
    y -= 543
    if ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)):    
        return 366 - day_of_year(d, m, y) + 1
    else:
        return 365 - day_of_year(d, m, y) + 1
    
def blue_zone_day(d, m, y):
    y -= 543
    return day_of_year(d, m, y) - 1

bd, bm, by, d, m, y = [int(e) for e in input().split()]

middle_years = y - by - 1

red = red_zone_day(bd, bm, by)
mid = middle_years*365
blue = blue_zone_day(d, m, y)

sum_days = red + mid + blue

physical = "{:.2f}".format(sin(2*pi*sum_days/23))
emotional = "{:.2f}".format(sin(2*pi*sum_days/28))
intellectual = "{:.2f}".format(sin(2*pi*sum_days/33))

print(sum_days, physical, emotional, intellectual)