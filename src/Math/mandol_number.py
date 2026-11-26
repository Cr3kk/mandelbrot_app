from math import sqrt

def calculate_mandolbrot_number(x, y, max_iter):
    distance = 0
    counter = 0
    a = 0
    b = 0
    while distance < 2:
        f_a = (a*a - b*b + x)
        f_b = (2 * a * b + y)
        counter += 1
    
        a = f_a
        b = f_b
        
        distance = sqrt(a**2 + b**2)
        if counter == max_iter:
            break
    if counter % 2 == 0:
        return "black"
    elif counter % 2 == 1:
        return "white"
    

    