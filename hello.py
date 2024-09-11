# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing the first element
first_fruit = fruits[0]
print(first_fruit)

# Modifying the second element
fruits[1] = "blueberry"
print(fruits)

# Adding a new element to the list
fruits.append("orange")
print(fruits)

# Removing an element by value
fruits.remove("cherry")
print(fruits)

# Removing an element by index
removed_fruit = fruits.pop(0)
print(fruits)
print("Removed fruit:", removed_fruit)

# Slicing the list
some_fruits = fruits[0:2]
print(some_fruits)

# Iterating through the list
for fruit in fruits:
    print(fruit)

# Checking if an element exists
if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")

# Getting the length of the list
length = len(fruits)
print("Number of fruits:", length)