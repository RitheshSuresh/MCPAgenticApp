# bad_code.py

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                if arr[i] not in duplicates:
                    duplicates.append(arr[i])
    return duplicates


def calculate_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


data = [1, 2, 3, 2, 4, 5, 1, 6]
print(find_duplicates(data))
print(calculate_sum(data))
print(check_prime(29))
