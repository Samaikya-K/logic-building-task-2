# Product prices
prices = [450, 1200, 899, 1500, 300]

# Step 1: Initialize counter
count = 0

# Step 2: Check each price
for price in prices:
    if price > 1000:
        count += 1

# Step 3: Display result
print("Products above 1000:", count)
