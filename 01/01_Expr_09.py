def str2hms(hms_str): 
    t = hms_str.split(':') 
    return int(t[0]),int(t[1]),int(t[2]) 
 
def hms2str(h, m, s): 
    return "{:02d}".format(h) + ":" + "{:02d}".format(m) + ":" + "{:02d}".format(s)

def to_sec(h, m, s) -> int: 
    return h*60*60 + m*60 + s
 
def to_hms(s): 
    h = s // (60*60)
    s -= h * 60*60
    m = s // 60
    s -= m * 60
    s = s
    
    return h, m, s

def diff(h1,m1,s1,h2,m2,s2): 
    
    dt = to_sec(h2, m2, s2) - to_sec(h1, m1, s1)
    return to_hms(dt)

def main(): 
    hms_start = input() 
    hms_end = input() 
    
    h1, m1, s1 = str2hms(hms_start)
    h2, m2, s2 = str2hms(hms_end)

    h, m, s = diff(h1, m1, s1, h2, m2, s2)

    print(hms2str(h, m, s))

exec(input())