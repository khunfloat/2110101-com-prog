def main():
    fname, year = input().strip().split()

    f = open(fname, "r")
    data = f.readlines()
    result = []

    for el in data:
        uid, score, *_ = el.split()
        uid, score = uid[:2], float(score)

        if year.endswith(uid):
            result.append(score)

    if result == []: 
        print("No data")
        return

    print(min(result), max(result), round(sum(result)/len(result), 2))
    return

main()