# Input string
text = "pythonp"

# Step 1: Create empty dictionary
char_count = {}

# Step 2: Count characters
for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

# Step 3: Display result
print(char_count)
