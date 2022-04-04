import math

def find_roots(a, b, c): # equation is in the form of ax2 + bx + c = 0
    d = (b ** 2) - (4 * a * c) # the discriminant
    if d < 0:
        return "No solution"
    
    ans1 = (-b + math.sqrt(d)) / (2 * a)
    ans2 = (-b - math.sqrt(d)) / (2 * a)

    return (ans1, ans2)

print(find_roots(2, 10, 8))
