def divisors(n):
    import math as M
    sqrtN = int(M.sqrt(n))
    divisors = []
    for i in range(1, sqrtN + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

n = int(input("Enter a number to find its divisors: "))
print(f"Divisors of {n}: {divisors(n)}")