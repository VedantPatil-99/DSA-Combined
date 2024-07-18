# Function to find the nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        last = fibonacci(n-1)
        slast = fibonacci(n-2)
        return last + slast

n = int(input("Enter the value of n: "))
print(f"{n}th Fibonacci number: {fibonacci(n)}")

# n = 3
# 3rd Fibonacci number: 2
