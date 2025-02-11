import sys

def getSides():
    sides = []
    for num, i in enumerate(range(3)):
        try:
            sides.append(int(input(f"Input Side {num+1} ")))
        except:
            sys.exit("Error inputting number")
    return sides

def determineTriangle(sides):
    for side in sides:
        if side <= 0:
            sys.exit("Side length needs to be greater than zero")
        
    sidec = max(sides)
    sides.remove(sidec)
    sidea = sides[0]
    sideb = sides[1]

    if (sidea == sideb) and (sideb == sidec) and (sidea == sidec):
        triangle = "Equilateral"
    elif (sidea == sideb) or (sideb == sidec) or (sidea == sidec):
        triangle = "Isoceles"
    elif ((sidea ** 2) + (sideb ** 2)) == (sidec ** 2):
        triangle = "Right angle"
    else:
        triangle = "Scalene"
    return triangle

triangle_message = f"{determineTriangle(getSides())}"
print(triangle_message)