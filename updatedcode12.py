def greet_users(names):
    for i in range(len(names)):
        print("Hello " + names[i])


def find_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers


names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5, 6]

# Keep existing behavior but demonstrate odd number finding
# This will print greetings and odd numbers found in the list

greet_users(names)
print(find_odd_numbers(numbers))
