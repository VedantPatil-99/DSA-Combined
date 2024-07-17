def isPrime(n):
    import math as M
    sqrtN = int(M.sqrt(n))
    count = 0
    for i in range(1, sqrtN + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    if count == 2:
        return True
    return False

n = int(input("Enter a number to check if it's prime: "))
print(f"Is {n} a prime number? {isPrime(n)}")