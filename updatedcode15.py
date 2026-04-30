# updatedcode15.py

def greet_users(names):
    for name in names:
        print(f"Hello {name}")


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

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
