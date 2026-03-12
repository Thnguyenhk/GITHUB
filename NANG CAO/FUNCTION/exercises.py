def calculate_total(price_list, tax_rate=0.08):
    subtotal = sum(price_list)
    if subtotal >= 100:
        subtotal = subtotal - 10
        print (f"Discount applied!")
    final_total = subtotal * (1 + tax_rate)
    return (f"Your total is {final_total} euros.")

print (calculate_total([50, 20, 30]))