# Given list of numbers
numbers = [3, 8, -2, 7, 0, -5, 10]

# 1. List of squares
squares = [n**2 for n in numbers]

# 2. List of positive numbers
positives = [n for n in numbers if n > 0]

# 3. Set of squares of even numbers
even_squares = {n**2 for n in numbers if n % 2 == 0}

# 4. Dictionary mapping each number to its cube
cubes = {n: n**3 for n in numbers}

# 5. Print results
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)