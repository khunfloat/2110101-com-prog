upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    result = ''

    string = input().strip()

    if string == 'end':
        break

    for char in string:
        if char.isupper():
            result += upperCase[(upperCase.index(char)+13)%26]
        elif char.islower():
            result += lowerCase[(lowerCase.index(char)+13)%26]
        else:
            result += char

    print(result)