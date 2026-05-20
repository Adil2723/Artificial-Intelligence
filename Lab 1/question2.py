def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, num))

numbers = []
print("Enter 10 integers:")

for _ in range(10):
    n = int(input())
    numbers.append(n)

for num in numbers:
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
