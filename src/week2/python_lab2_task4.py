
prices = [12.5, 9.9, 15.0, 22.3, 5.0]
quantities = [2, 5, 1, 3, 4]

# 1. Compute total cost for each item using map() and lambda
totals = list(map(lambda p_q: p_q[0] * p_q[1], zip(prices, quantities)))

# 2. Filter totals above 30 using filter()
high_totals = list(filter(lambda total: total > 30, totals))

# 3. Pair prices and quantities using zip()
pairs = list(zip(prices, quantities))

# 4. Repeat using list comprehensions
totals_comp = [p * q for p, q in zip(prices, quantities)]
high_totals_comp = [total for total in totals_comp if total > 30]

# 5. Print results
print("Totals:", totals)
print("Totals > 30:", high_totals)
print("Price-quantity pairs:", pairs)
print("Totals (comprehension):", totals_comp)
print("Totals > 30 (comprehension):", high_totals_comp)
