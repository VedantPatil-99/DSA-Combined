def count_digits(n):
    cnt = 0
    while n > 0:
        lastdigit = n % 10
        n //= 10
        cnt += 1
    return cnt

n = int(input("Enter a number to count its digits: "))
digits = count_digits(n)
print(f"Number of digits in {n}: {digits}")


def print_digits(n):
    while n > 0:
        lastdigit = n % 10
        n //= 10
        print(lastdigit, end=" ")
    print()

n = int(input("Enter a number to print its digits: "))
print(f"Digits of {n}:")
print_digits(n)