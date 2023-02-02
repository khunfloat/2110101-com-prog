string = input().strip()

if not ('(' in string or ')' in string or '[' in string or ']' in string):
    print(string)
else:
    string = list(string)
    for i in range(len(string)):
        if string[i] == ')':
            string[i] = ']'
        elif string[i] == '(':
            string[i] = '['
        elif string[i] == ']':
            string[i] = ')'
        elif string[i] == '[':
            string[i] = '('
    print("".join(string))