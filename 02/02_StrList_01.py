n = [int(d) for d in input()]

check_digit = (11 - ((13*n[0]+12*n[1]+11*n[2]+10*n[3]+9*n[4]+8*n[5]+7*n[6]+6*n[7]+5*n[8]+4*n[9]+3*n[10]+2*n[11]) % 11)) % 10

a = str(n[0])
b = "".join([str(d) for d in n[1:5]])
c = "".join([str(d) for d in n[5:10]])
d = "".join([str(d) for d in n[10:]])
e = str(check_digit)

print(a, b, c, d ,e)