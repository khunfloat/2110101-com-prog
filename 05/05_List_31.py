cards = [e for e in input().strip().split(' ')]
mode = list(input().strip())

def cut(card_list):
    group_n = int(len(card_list)//2)
    card_list[group_n:], card_list[:group_n], = card_list[:group_n], card_list[group_n:]
    return card_list

def rid(card_list):
    group_n = int(len(card_list)//2)
    front, back = card_list[:group_n], card_list[group_n:]
    res = []
    for i in range(0, len(front)):
        res.append(front[i])
        res.append(back[i])
    return res

for m in mode:
    if m == 'C':
        cards = cut(cards)
    if m == 'S':
        cards = rid(cards)

print(' '.join(cards))