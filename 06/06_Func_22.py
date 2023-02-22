def distance1(x1, y1, x2, y2): 
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def distance2(p1, p2): 
    return distance1(*p1, *p2)

def distance3(c1, c2): 
    dist = distance1(*c1[:2], *c2[:2])
    if dist <= (c1[2] + c2[2]):
        return dist, True
    else:
        return dist, False

def perimeter(points): 
    dist = 0
    for i in range(len(points)):
        dist += distance2(points[i-1], points[i])
    return dist

exec(input().strip())