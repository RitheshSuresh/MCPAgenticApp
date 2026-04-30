# updatedcode14.py

def greet_users(names):
    for name in names:
        print("Hello " + name)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5, 6]

greet_users(names)
print(find_prime_numbers(numbers))
