def check_digit(i):
    n = [int(d) for d in i]

    check_digit = (11 - ((13*n[0]+12*n[1]+11*n[2]+10*n[3]+9*n[4]+8*n[5]+7*n[6]+6*n[7]+5*n[8]+4*n[9]+3*n[10]+2*n[11]) % 11)) % 10

    return check_digit

exec(input())