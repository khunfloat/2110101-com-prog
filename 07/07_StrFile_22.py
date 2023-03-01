def a(first, second):
    first = first.lower().replace(' ', '')
    second = second.lower().replace(' ', '')
    for char in first.lower():
        if first.count(char) != second.count(char):
            return "NO"
    return "YES"

print(a(input().strip(), input().strip()))