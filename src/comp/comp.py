# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [f"{i.name}" for i in humans if i.name[0] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [f"{i.name}" for i in humans if i.name[len(i.name) - 1] == "e"]

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive
##checking ord('C') and ord('G') in python REPL,, C == 67 and G == 71
print("Starts between C and G, inclusive:")
alph_range = []
c = []
for letter in range(67,72):
    alph_range.append(chr(letter)) # converts to letter equivelant

for letter in alph_range:
    d = [c.append(f"{i.name}") for i in humans if i.name[0] == letter]
print(c)
    

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [a.age + 10 for a in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{i.name}-{i.age}" for i in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

# print("Names and ages between 27 and 32:")

num_range = []
for number in range(27,33):
    num_range.append(number)

f = []
for number in num_range:
    i = [f.append((f"{i.name}", i.age)) for i in humans if i.age == number]
print(f)




# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [(i.name.upper(), i.age + 5) for i in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(i.age) for i in humans]
print(h)
