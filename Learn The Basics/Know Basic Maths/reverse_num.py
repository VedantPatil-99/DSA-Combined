def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = (rev * 10) + digit
        n //= 10
    return rev

n = int(input("Enter a number to reverse it: "))
print(f"Reversed {n}: {reverse_number(n)}")