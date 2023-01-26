subscriber = int(input())

if subscriber // 10000000000 > 0:
    print(str(round(subscriber / 1000000000))+'B')
elif subscriber // 1000000000 > 0:
    print(str(round(subscriber / 1000000000, 1))+'B')

elif subscriber // 10000000 > 0:
    print(str(round(subscriber / 1000000))+'M')
elif subscriber // 1000000 > 0:
    print(str(round(subscriber / 1000000, 1))+'M')

elif subscriber // 10000 > 0:
    print(str(round(subscriber / 1000))+'K')
elif subscriber // 1000 > 0:
    print(str(round(subscriber / 1000, 1))+'K')

else:
    print(subscriber)