def rotate_left(s, n):
    return s[n:] + s[:n]

def rotate_right(s, n):
    return s[-n:] + s[:-n]

def str_mod(s, n):
    return "".join([str(int(e)%n) for e in s])

def main():
    
    s = input().strip()

    if s[-2] == "1":
        print(rotate_left(s, n))
    elif s[-2] == "2":
        print(rotate_right(s, n))
    elif s[-2] == "3":
        print(str_mod(s, n))
    else:
        print(s)