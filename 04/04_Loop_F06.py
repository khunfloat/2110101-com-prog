def print_triangle(h):
    print('.'*(h-1)+'*')
    for i in range(1, h-1):
        string = '.'*(h-i-1)+'*'+'.'*(2*i-1)+'*'
        print(string)
    print('*'*(2*h-1))

exec(input())