import math
def calculate_area(shape: str, dimension1:float, dimension2:float=1.0)->float:
    if isinstance(shape, str) and (isinstance(dimension1, int) or isinstance(dimension1, float) ) and (isinstance(dimension2, int) or isinstance(dimension2, float)):
        if shape.lower() == "rectange":
            return dimension1 * dimension2
        elif shape.lower() == "square":
            return dimension1 ** 2
        elif shape.lower() == "triangle":
            base = dimension1
            height = dimension2
            return (base/2) * height
        elif shape.lower() == "circle":
            radius = dimension1
            return math.pi * (radius ** 2)
        return -1.0
    else:
        return -1.0


res1 = calculate_area("square", 5)
print(res1)
res1 = calculate_area("rectangle", 5, 6)
print(res1)
res1 = calculate_area("triangle", 5, 3)
print(res1)
res1 = calculate_area("circle", 4)
print(res1)

