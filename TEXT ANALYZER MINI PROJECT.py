print("TEXT ANALYZER")

# Write to file
file = open("text.txt","w")
text = input("Enter text: ")
file.write(text)
file.close()

print("Data written to file")

print("------")

# Read file
file = open("text.txt","r")
data = file.read()
file.close()

print("File Content:")
print(data)

print("------")

# Word count
words = data.split()
print("Word count:", len(words))

print("------")

# Line count
lines = data.split("\n")
print("Line count:", len(lines))

print("------")

# Character count
print("Character count:", len(data))

#added more features
print("more features")

# Vowel count
count = 0
for i in data:
    if i.lower() in "aeiou":
        count += 1
print("Vowel count:", count)

print("------")

# Count specific word
word = input("Enter word to search: ")
print("Count:", data.count(word))

print("------")

# Uppercase and Lowercase
print("Uppercase:")
print(data.upper())

print("Lowercase:")
print(data.lower())

print("------")

# Replace word
old = input("Enter word to replace: ")
new = input("Enter new word: ")
new_data = data.replace(old, new)

print("After replace:")
print(new_data)
