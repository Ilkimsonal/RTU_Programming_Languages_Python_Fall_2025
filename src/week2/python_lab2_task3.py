# 1. Get input from the user
expression = input("Enter an arithmetic expression: ")

# 2. Define possible operator symbols
operators = ['+', '-', '*', '/', '(', ')']

# 3. Initialize frequency dictionary with 0 counts
operator_counts = {op: 0 for op in operators}

# 4. Count operator occurrences
for char in expression:
    if char in operators:
        operator_counts[char] += 1

# 5. Print results
print("Operator counts:", operator_counts)