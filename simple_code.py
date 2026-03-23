# simple_code.py

def greet_users(names):
    for i in range(len(names)):
        print("Hello " + names[i])


def find_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5, 6]

greet_users(names)
print(find_even_numbers(numbers))
