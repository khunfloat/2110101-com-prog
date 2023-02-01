mode = input().strip()
string = []

len_check = 0

for _ in range(0, int(input().strip())):
    text = input().strip()
    len_check += len(text)
    string.append(text)

if len_check != len(string)*len(string[0]):
    print("Invalid size")

else:
    if mode == '90':
        for y in range(0, len(string[0])):
            result = ''
            for i in range(0, len(string)):
                result += string[len(string) - 1 - i][y]
            print(result)

    elif mode == 'flip':
        for i in string:
            print(i[::-1])

    elif mode == '180':
        for i in string[::-1]:
            print(i[::-1])