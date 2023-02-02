def RLE(string):
    string += ' '
    char_splited = []
    recent_char = ''
    for char in list(string):
        if recent_char != '':
            if char != recent_char[0]:
                char_splited.append(recent_char)
                recent_char = char
            elif char == recent_char[0]:
                recent_char += char
        else:
            recent_char = string[0]
    result = []
    for string in char_splited:
        result.append([string[0], len(string)])
    return result

exec(input())