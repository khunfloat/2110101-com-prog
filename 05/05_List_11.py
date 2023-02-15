chars = list(input())

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for char in chars:
    if char.isdigit():
        try:
            a.remove(char)
        except ValueError:
            pass

if a == []:
    print("None")
else:
    print(','.join(a))