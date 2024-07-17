def armstrong_number(n):
    sum = 0
    power = len(str(n))
    copy = n
    while copy > 0:
        digit = copy % 10
        sum += (digit ** power)
        copy //= 10
    if n == sum:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is NOT an Armstrong number.")

n = int(input("Enter a number to check if it's an Armstrong number: "))
armstrong_number(n)