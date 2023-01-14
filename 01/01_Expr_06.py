t1 = int(input())*60*60 + int(input())*60 + int(input())
t2 = int(input())*60*60 + int(input())*60 + int(input())

dt = t2 - t1
if dt < 0: dt = 24*60*60 + dt

dh = dt // (60*60)
dt -= dh * 60*60
dm = dt // 60
dt -= dm * 60
ds = dt

print(f"{dh}:{dm}:{ds}")