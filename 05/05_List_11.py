chars = list(input())

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for char in chars:
    if char.isdigit():
        try:
            a.remove(char)
        except ValueError:
            pass

if chars == []:
    print("None")
else:
    print(', '.join(a))