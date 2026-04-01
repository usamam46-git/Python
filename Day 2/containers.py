# A list (container) of fruits
fruits = ["apple", "banana", "mango", "orange"]

print("Here are the fruits in the list:")

# Loop through the container
for fruit in fruits:
    print(fruit)

# Add a new item
fruits.append("grapes")

print("\nAfter adding grapes:")
print(fruits)

# Check if an item exists
search = input("\nEnter a fruit to search: ")

if search in fruits:
    print("Yes! It's in the list.")
else:
    print("Nope, not found.")