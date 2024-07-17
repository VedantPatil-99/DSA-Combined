def isPalindrome(n):
    rev = 0
    copy = n
    while copy > 0:
        digit = copy % 10
        rev = (rev * 10) + digit
        copy //= 10
    if n == rev:
        print(f"{n} is a palindrome number.")
    else:
        print(f"{n} is NOT a palindrome number.")

n = int(input("Enter a number to check if it's a palindrome: "))
isPalindrome(n)