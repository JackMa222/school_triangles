import sys

class Triangle:
    def __init__(self, side1, side2, side3):
        self.original_sides = sorted([side1, side2, side3])
        self.sides = self.convertSidesToFloat()
        self.side_a, self.side_b, self.side_c = self.sides
        self.triangleType = self.determineTriangle()
        
    def convertSidesToFloat(self):
        sides = []
        for side in self.original_sides:
            try:
                floatNum = float(side)
            except:
                # this string will be caught in validateSides
                floatNum = 'Not a number'
            sides.append(floatNum)
        return sides

    
    def validateSides(self):
        if any(type(side) not in [float, int] for side in self.sides):
            return (False, "Sides must be a number")
        if any(side <= 0 for side in self.sides):
            return (False, "Sides cannot be zero or negative")
        if self.side_a + self.side_b <= self.side_c:
            return (False, "Triangle is physically invalid")
        return (True, "")
    
    def determineTriangle(self):
        if self.validateSides()[0] is False:
            return self.validateSides()[1]
        
        if self.side_a == self.side_b == self.side_c:
            triangle = "Equilateral"
        elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_a == self.side_c:
            triangle = "Isoceles"
        elif (self.side_a ** 2) + (self.side_b ** 2) == (self.side_c ** 2):
            triangle = "Right angle"
        else:
            triangle = "Scalene"
        return triangle
    
    def getSides():
        sides = []
        for num in range(3):
            try:
                sides.append(float(input(f"Enter Side {num}")))
            except ValueError:
                sys.exit("Input must be a valid number")