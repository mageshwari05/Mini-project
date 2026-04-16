print("FILE READER MINI PROJECT")
print("------")
# Read file
file = open("data.txt","r")
data = file.read()
print("File Content:")
print(data)
file.close()
print("------")
# Read line by line
file = open("data.txt","r")
print("Read Line by Line:")
for line in file:
    print(line)
file.close()
print("------")
# Count lines
file = open("data.txt","r")
count = 0
for line in file:
    count = count + 1
print("Total Lines:",count)
file.close()
print("------")
# Count words
words = data.split()
print("Total Words:",len(words))
print("------")
# Count characters
print("Total Characters:",len(data))
print("------")
# Count vowels
vowels = 0
for i in data:
    if i.lower() in "aeiou":
        vowels = vowels + 1
print("Total Vowels:",vowels)
print("------")
