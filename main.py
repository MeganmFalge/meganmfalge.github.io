# Megan Falge
# A text-based adventure game.
# The user will have to go through a maze to avoid death.

# Simple I/O
print("Hello User,", sep=' ', end=' ')
print("Welcome!", end='\n')

# string operators
name = input("What is your name? ")
age = input("What is your age? ")
print("User:", name + ' ' + age)
# prints age and name on the same line together

print("Today you," + ' ' + name + ', will be escaping an island.')

# if-elif statement
response_one = input("Do you think you can escape? ")
if response_one == "yes":
    print("Lets go!")
elif response_one != "yes":
    print("Try again. " * 2)

print("Before we start let pick on item for you to start with.")

# starting item
item_a = 'Knife'
item_b = 'Book'
item_c = 'Bottle'

print("You have a choice between 3 items")
print("Item 1:", item_a)
print("Item 2:", item_b)
print("Item 3:", item_c)

# if-elif-else statement
response_two = input("Which item will be picking? ")
if response_two == "knife":
    print("Nice choice!")
elif response_two == "book":
    print("Smart choice!")
elif response_two == "bottle":
    print("Hydrated choice!")
else:
    print("Try again.")

input("To start adventure type 'Go': ")

# Intro to maze
print("Enter the maze", name, end="\n")
print("Where will you go?")

# Basic Calculations
print(10 ** 2)
# exponent

print(3 * 6)
# multiplication

print(6 / 2)
# division

print(4 % 7)
# modulus

print(8 // 2)
# floor division

print(4 + 3)
# addition

print(8 - 5)
# subtraction

# Boolean Operators
print(10 >= 4)
# prints if its true or false that ten is greater than or equal to four

# Standard iterative structures
x = 5
print(x > 3 and x < 10)
# prints if its true or false

while x >= 5:
    print(x > 2 or x < 4)
    break
# prints if its true or false

while x == 5:
    print(not(x > 3 and x < 10))
    break
# prints if its true or false

# For loops
supplies = ["Compass","Map"]
for x in supplies:
    if x == "Map":
        continue
    print(x)
    if x == "Compass":
        break

for x in range(4):
    print(x)