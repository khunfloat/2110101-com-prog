summer = []

while True:
    number = input()

    if number != 'q':
        summer.append(float(number))

    elif number == 'q':
        if summer == []:
            print('No Data')
            break
        else:
            print(round(sum(summer)/len(summer), 2))
            break