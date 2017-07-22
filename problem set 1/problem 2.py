# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

s = "azcbobobegghaklbob"
length = len(s)
lookup = "bob"
index = 0
count = 0

while index < length - 2:
    if s[index:index + 3] == "bob":
        count += 1
    index += 1

print("Number of times bob occurs is: " + str(count))