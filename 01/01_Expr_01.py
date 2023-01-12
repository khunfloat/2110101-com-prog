from math import sqrt, pi, e

n = int(input())

lower = sqrt(2*pi)*(n**(n+0.5))*(e)**(-n+(1/(12*n+1)))
upper = sqrt(2*pi)*(n**(n+0.5))*(e)**(-n+(1/(12*n)))

print(lower)
print(upper)