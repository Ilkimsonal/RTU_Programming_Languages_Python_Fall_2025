import math

def circle_area(radius):
    """Return the area of a circle given its radius."""
    area = math.pi * (radius ** 2)
    return area

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    result = circle_area(radius)
    print(f"The area of the circle is {result:.2f}")

