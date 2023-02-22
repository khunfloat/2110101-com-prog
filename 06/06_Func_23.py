def make_int_list(x):
    return [int(e) for e in x.strip().split()]

def is_odd(e): 
    return True if e % 2 != 0 else False

def odd_list(alist): 
    return [e for e in alist if is_odd(e)]
 
def sum_square(alist): 
    return sum([e**2 for e in alist])
 
exec(input().strip())