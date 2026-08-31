def calculate_total(*prices):
    if not prices:
        return 'Your cart is empty.'

    total = sum(prices)

    if total > 200:
        total *= 0.8  # 20% discount
    elif total > 100:
        total *= 0.9  # 10% discount

    return f'Final total: ${total:.2f}'

# Testing the result
print(calculate_total(30, 20, 50))
print(calculate_total(100, 50, 80))
print(calculate_total(150, 100))
print(calculate_total())