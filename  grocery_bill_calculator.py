# Sample data
item_prices = [100, 200, 50]       # prices for item 1, 2, 3
quantities = [2, 1, 4]             # quantities for item 1, 2, 3
discount_rate = 10                 # 10%
tax_rate = 5                       # 5%

# Step 1: Calculate subtotal
subtotal = sum([price * qty for price, qty in zip(item_prices, quantities)])

# Step 2: Apply discount
discount_amount = (discount_rate / 100) * subtotal
subtotal_after_discount = subtotal - discount_amount

# Step 3: Apply tax
tax_amount = (tax_rate / 100) * subtotal_after_discount
total_cost = subtotal_after_discount + tax_amount

# Output
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount ({discount_rate}%): -₹{discount_amount:.2f}")
print(f"Tax ({tax_rate}%): +₹{tax_amount:.2f}")
print(f"Total Cost to Customer: ₹{total_cost:.2f}")
