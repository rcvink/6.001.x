# Assume s is a string of lower case characters

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o',
# and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

s = "azcbobobegghakl"
length = len(s)
index = 0
vowels = 0
listofvowels = ["a", "e", "i", "o", "u"]

while index < length:
    if s[index] in listofvowels:
        vowels += 1
    index += 1

print("Number of vowels: " + str(vowels))