import json
# Creating a dictionary of fruits
fruits = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red"
}
print(fruits)

# Accessing the value of a key
apple_color = fruits["apple"]
print(apple_color)

# Modifying the value of a key
fruits["banana"] = "green"
print(fruits)

# Adding a new key-value pair
fruits["orange"] = "orange"
print(fruits)

# Removing an element by key
del fruits["cherry"]
print(fruits)

# Removing an element by key and getting its value
banana_color = fruits.pop("banana")
print(fruits)
print("Removed banana color:", banana_color)

# Iterating through the keys
for fruit in fruits:
    print(fruit)

# Iterating through the values
for color in fruits.values():
    print(color)

# Iterating through the key-value pairs
for fruit, color in fruits.items():
    print(fruit, "is", color)
    
# Checking if a key exists
if "apple" in fruits:
    print("Apple is in the dictionary")
else:
    print("Apple is not in the dictionary")
    
# Getting the length of the dictionary
length = len(fruits)
print("Number of fruits:", length)

# Reading the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)
print(data)

students = data["students"]

# Iterating through the list of students
for student in students:
    print(student["name"])
    print(student["age"])
    