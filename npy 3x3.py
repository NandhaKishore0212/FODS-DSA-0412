import numpy as np

# Step 1: Create a sample 3x3 NumPy array
# Each row = product, each column = price of each sale for that product
sales_data = np.array([
    [100, 150, 200],   # Product 1
    [80, 120, 160],    # Product 2
    [90, 140, 190]     # Product 3
])

# Step 2: Calculate the average price of all products sold
average_price = np.mean(sales_data)

# Step 3: Print the result
print(f"Average price of all products sold: ₹{average_price:.2f}")
