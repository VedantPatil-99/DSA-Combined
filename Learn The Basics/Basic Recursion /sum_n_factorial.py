
# Function to find the sum of first N natural numbers using recursion
def find_sum(N):
    if N == 0:
        return 0
    return N + find_sum(N-1)

N = int(input("Enter the value of N: "))
print(f"Sum of first {N} natural numbers: {find_sum(N)}")

# N = 10
# Sum of first 10 natural numbers: 55




# Function to find the factorial of a number using recursion
def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)

N = int(input("Enter the value of N: "))
print(f"Factorial of {N}: {factorial(N)}")

# N = 5
# Factorial of 5: 120