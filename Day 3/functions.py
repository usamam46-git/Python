
def add(a, b):
    return a + b

print("Add:", add(3, 5))


# 2. Write a function to check if a number is even
def is_even(num):
    return num % 2 == 0

print("Is 4 even?", is_even(4))


# 3. Write a function to find the maximum of 3 numbers
def find_max(a, b, c):
    return max(a, b, c)

print("Max:", find_max(3, 7, 5))

# 4. Function to return sum of a list
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Sum:", sum_list([1, 2, 3, 4]))


# 5. Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

print("Vowels:", count_vowels("Hello World"))

# 6. Simple lambda function for square
square = lambda x: x * x
print("Square:", square(5))


# 7. Lambda for adding two numbers
add_lambda = lambda a, b: a + b
print("Lambda Add:", add_lambda(2, 3))

numbers = [1, 2, 3, 4, 5]

# 8. Use map + lambda to square all numbers
squared = list(map(lambda x: x * x, numbers))
print("Squared List:", squared)


# 9. Use filter + lambda to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", evens)


# 10. Use sorted + lambda (sort by last digit)
nums = [23, 45, 12, 67, 34]
sorted_nums = sorted(nums, key=lambda x: x % 10)
print("Sorted by last digit:", sorted_nums)

# 11. Function to reverse a string
def reverse_string(s):
    return s[::-1]

print("Reverse:", reverse_string("Python"))


# 12. Function to check palindrome
def is_palindrome(s):
    return s == s[::-1]

print("Is palindrome:", is_palindrome("madam"))


# 13. Lambda to get length of string
length = lambda s: len(s)
print("Length:", length("Hello"))


# 14. Use lambda + map to convert all names to uppercase
names = ["usama", "ali", "ahmed"]
upper_names = list(map(lambda name: name.upper(), names))
print("Uppercase Names:", upper_names)


# 15. Use lambda + filter to get numbers greater than 10
nums2 = [5, 12, 7, 18, 3, 20]
greater_than_10 = list(filter(lambda x: x > 10, nums2))
print("Greater than 10:", greater_than_10)
print("\n--- End of Day 3 Exercises ---")