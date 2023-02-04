def missing_digits(t):
    chars = list(t)

    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for char in chars:
        if char.isdigit():
            try:
                a.remove(char)
            except ValueError:
                pass

    if chars == []:
        return []
    else:
        return a

exec(input())