from math import gcd

i = input()
i = i.split(',')
multiplier1 = 10**(len(i[1]) + len(i[2]))
multiplier2 = 10**len(i[1])

value1 = int(i[0]+i[1]+i[2])
value2 = int(i[0]+i[1])

denominator = multiplier1 - multiplier2
remainder = (value1 - value2)

portion = gcd(remainder, denominator)

remainder, denominator = remainder//portion, denominator//portion

print(remainder, '/', denominator)