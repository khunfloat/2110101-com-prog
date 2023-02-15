def peaks(data):
    res = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            res.append(i)
    return res

exec(input())