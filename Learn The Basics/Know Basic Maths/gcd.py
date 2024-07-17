def find_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    return a

a = int(input("Enter the first number to find GCD: "))
b = int(input("Enter the second number to find GCD: "))
print(f"GCD of {a} and {b}: {find_gcd(a, b)}")