name = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nickname = ['Dick', 'Dill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']

a = []

for _ in range(int(input())):
    a.append(input().strip())

for n in a:
    if n in name:
        i = name.index(n)
        print(nickname[i])
    elif n in nickname:
        i = nickname.index(n)
        print(name[i])
    else: print('Not found')