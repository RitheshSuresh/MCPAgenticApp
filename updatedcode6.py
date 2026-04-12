# prime numbers version of simple_code.py

def greet_users(names):
    for i in range(len(names)):
        print("Hello " + names[i])


def find_prime_numbers(numbers):
    # Returns all prime numbers from the input list
    primes = []
    for num in numbers:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

greet_users(names)
print(find_prime_numbers(numbers))
