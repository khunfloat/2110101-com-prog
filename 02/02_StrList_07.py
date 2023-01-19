i = input()

a = int(i[3::7])
b = int(i[7::5])
c = a + b + 10000

h, t, d = (c // 1000) % 10, (c // 100) % 10, (c // 10) % 10

res = ((h + t + d) % 10) + 1

print(str(h)+str(t)+str(d)+['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'][res])