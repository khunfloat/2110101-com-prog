string = input().strip().replace('"', ' ').replace('-', ' ').replace('.', ' ').replace(')', ' ').replace('(', ' ').replace('>', ' ').replace(';', ' ').split()

result = string[0].lower()

for word in string[1:]:
    if word[0].isalpha():
        result += word[0].upper() + word[1:].lower()
    else:
        result += word

print(result)