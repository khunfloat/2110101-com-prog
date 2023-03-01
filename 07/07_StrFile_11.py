word = input().strip()

if word.endswith('x') or word.endswith('s') or word.endswith('ch'):
    print(word + 'es')
elif word.endswith('y'):
    if word[-2] in 'aeiou':
        print(word + 's')
    else:
        print(word[:-1] + 'ies')
else:
    print(word + 's')