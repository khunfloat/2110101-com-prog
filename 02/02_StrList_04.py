m = input()
n = int(input())
formater = "{:0" + str(max(len(m), n)) + "d}"
print(formater.format(int(m)))