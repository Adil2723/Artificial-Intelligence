def fibonacci_upto(n):

    a, b = 0, 1
    fib_sequence = []

   
    while a <= n:
        fib_sequence.append(a)  
        a, b = b, a + b       

    return fib_sequence

num = int(input("Enter a number: "))

print(f"Fibonacci sequence up to {num}: {fibonacci_upto(num)}")
