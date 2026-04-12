def greet_users(names):
    for i in range(len(names)):
        print("Hello " + names[i])


def find_primes(numbers):
    primes = []
    for n in numbers:
        if n < 2:
            continue
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes


names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5, 6]

greet_users(names)
print(find_primes(numbers))
