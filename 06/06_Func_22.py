def distance1(x1, y1, x2, y2): 
    dx = float(x2) - float(x1)
    dy = float(y2) - float(y1)

    distance = (dx**2 + dy**2)**0.5

    return distance

def distance2(p1, p2): 

    return distance1(*p1, *p2)
      
def distance3(c1, c2): 
    x1, y1, r1 = c1
    x2, y2, r2 = c2

    distance = distance1(x1, y1, x2, y2)

    if distance <= r1 + r2:
        return distance, True

    return distance, False

def perimeter(points): 
    perimeter = 0
    for i in range(len(points)):
        perimeter += distance2(points[i-1], points[i])
    
    return perimeter

 
exec(input().strip())