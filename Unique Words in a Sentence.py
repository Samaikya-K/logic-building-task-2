# Step 1: Take input
sentence = input("Enter sentence: ")

# Step 2: Convert to lowercase
sentence = sentence.lower()

# Step 3: Split into words
words = sentence.split()

# Step 4: Get unique words using set
unique_words = set(words)

# Step 5: Display results
print("Unique words count:", len(unique_words))
print("Unique words:", unique_words)
