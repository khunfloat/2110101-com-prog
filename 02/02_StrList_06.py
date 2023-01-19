u = input()
u = [float(i) for i in u.strip('][').split(', ')]
v = input()
v = [float(i) for i in v.strip('][').split(', ')]

result = [u[i]+v[i] for i in range(3)]

print(u, '+', v, '=', result)