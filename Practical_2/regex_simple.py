import re

# Example 1: Finding a pattern in a string
text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"
matches = re.findall(pattern, text)
print("Example 1:")
print("Found:", matches)


# Example 2: Matching a specific pattern
text = "Email me at user@example.com or user2@example.org"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
matches = re.findall(pattern, text)
print("\nExample 2:")
print("Found emails:", matches)

# Example 3: Splitting a string using regex
text = "Split this, sentence into, separate parts!"
pattern = r"\W+"
parts = re.split(pattern, text)
print("\nExample 3:")
print("Parts:", parts)

# Example 4: Substituting a pattern in a string
text = "Replace all numbers like 1234 and 5678 with X"
pattern = r"\d+"
replacement = "X"
new_text = re.sub(pattern, replacement, text)
print("\nExample 4:")
print("New text:", new_text)

# Example 5: Matching groups in a string
text = "John has 5 apples, Jane has 3 oranges."
pattern = r"(\w+) has (\d+) (\w+)"
matches = re.findall(pattern, text)
print("\nExample 5:")
for match in matches:
    name, quantity, fruit = match
    print(f"{name} has {quantity} {fruit}")