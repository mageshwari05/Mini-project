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
