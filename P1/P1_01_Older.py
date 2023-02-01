name_1, month_1, date_1, year_1  = input().split(' ')
name_2, month_2, date_2, year_2  = input().split(' ')

month_mapper = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

date_1, date_2 = int(date_1[:-1]), int(date_2[:-1])
month_1, month_2 = month_mapper[month_1], month_mapper[month_2]
year_1, year_2 = int(year_1), int(year_2)

if (date_1 == date_2) and (month_1 == month_2) and (year_1 == year_2):
    print(name_1, name_2)
else:
    if year_1 < year_2:
        print(name_1)
    elif year_1 > year_2:
        print(name_2)
    else:
        if month_1 < month_2:
            print(name_1)
        elif month_1 > month_2:
            print(name_2)
        else:
            if date_1 < date_2:
                print(name_1)
            elif date_1 > date_2:
                print(name_2)