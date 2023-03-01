# data1 = open("07/data1.txt", "r").readlines()
# data2 = open("07/data2.txt", "r").readlines()

fname1, fname2 = input().strip().split()
data1 = open(fname1, "r").readlines()
data2 = open(fname2, "r").readlines()

all_data = data1+data2

cleaned_data = [[e.strip().split()[0], "{:.2f}".format(float(e.strip().split()[1]))] for e in all_data]

def sort_by_faculty(data):
    return data[0][-2:], int(data[0])

cleaned_data.sort(key=sort_by_faculty)

for sid, grade in cleaned_data:
    print(sid, grade)