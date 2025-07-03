import numpy as np

# Dummy data: [bedrooms, square_footage, sale_price]
house_data = np.array([
    [3, 1200, 250000],
    [5, 2000, 400000],
    [4, 1500, 320000],
    [6, 3000, 550000]
])

# Filter rows where number of bedrooms > 4
filtered_data = house_data[house_data[:, 0] > 4]

# Extract the sale prices of those houses
sale_prices = filtered_data[:, 2]

# Calculate the average sale price
average_price = np.mean(sale_prices)

print("Average sale price of houses with more than 4 bedrooms:", average_price)
