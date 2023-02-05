def is_prime(n): 
    if n <= 1: 
        return False 
    for k in range(2,int(n**0.5)+1): 
        if n%k == 0: 
            return False 
    return True 
 
def next_prime(N): 
    N += 1
    while not is_prime(N):
        N += 1
    return N
 
def next_twin_prime(N): 

    a, b = N, N + 1
    
    while b - a != 2:
        a = next_prime(a)
        b = next_prime(a)

    return (a, b)
 
exec(input().strip())