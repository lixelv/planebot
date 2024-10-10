import re

letters = ["x", "y", "z", "d"]

def calculate_plane(x0, y0, z0, x1, y1, z1, x2, y2, z2):
    a = ((z2-z0)*(y1-y0)-(z1-z0)*(y2-y0))
    b = ((x2-x0)*(z1-z0)-(x1-x0)*(z2-z0))
    c = ((y2-y0)*(x1-x0)-(y1-y0)*(x2-x0))
    d = -(a*x0+b*y0+c*z0)
    
    result = [a, b, c, d]
    
    i = 2
    smallest = min([abs(j) for j in result if j != 0])
    
    while i <= smallest:
        for j in result:
            if j % i != 0:
                break
        else:
            result = [j//i for j in result]
            i-=1
        
        i += 1
    
    if len([i for i in result if i < 0]) > (len([i for i in result if i != 0])//2):
        result = [-j for j in result]
    
    return result
    
def calculate_plane2(string):
    numbers = list(map(int, re.findall(r"-?\d+", string)))
    try:
        result = calculate_plane(*numbers)
        result_str = ""
        
        for i, j in enumerate(result):
            if j != 0:
                if result_str != "":
                    result_str += " + " + str(j) + letters[i]
                else:
                    result_str += str(j) + letters[i]
            
        if result_str == "":
            return "Плоскость не существует"
        else:
            return result_str + " = 0"
    
    except TypeError:
        return "Неверный формат"
