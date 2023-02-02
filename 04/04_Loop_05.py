interested_word = input().strip()
sentence = input().strip()
sentence = sentence.replace('.', ' ')
sentence = sentence.replace('(', ' ')
sentence = sentence.replace(')', ' ')
sentence = sentence.replace(',', ' ')
sentence = sentence.replace("'", ' ')
sentence = sentence.replace('"', ' ')
sentence = sentence.split()

count = 0

for word in sentence:
    if word == interested_word:
        count += 1

print(count)