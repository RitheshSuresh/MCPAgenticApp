def find_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers


def greet_users(names):
    for i in range(len(names)):
        print("Hello " + names[i])


names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5, 6]

print("Greet:")
greet_users(names)
print("Odd numbers:")
print(find_odd_numbers(numbers))
