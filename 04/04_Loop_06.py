# 8


# .......* 

# ......*.* 
# .....*...* 
# ....*.....* 
# ...*.......* 
# ..*.........* 
# .*...........* 

# ***************

h = int(input())
print('.'*(h-1) + '*')
for i in range(h-2):
    print('.'*(h-2-i) + '*' + '.'*(2*(i+1)-1) + '*')
print('*'*(2*h-1))

# h = int(input()) 
# print('.'*(h-1)+'*')
# for i in range(1, h-1):
#     string = '.'*(h-i-1)+'*'+'.'*(2*i-1)+'*'
#     print(string)
# print('*'*(2*h-1))