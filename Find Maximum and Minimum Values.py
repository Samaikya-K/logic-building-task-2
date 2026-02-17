# List of numbers
numbers = [45, 22, 89, 10, 66]

# Step 1: Initialize max and min
maximum = numbers[0]
minimum = numbers[0]

# Step 2: Loop through list
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

# Step 3: Display results
print("List:", numbers)
print("Max:", maximum)
print("Min:", minimum)
