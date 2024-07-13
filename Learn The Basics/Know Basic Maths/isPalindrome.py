def isPalindrome(n):
  rev = 0
  copy = n
  while copy > 0:
    digit = copy % 10
    rev = (rev * 10) + digit
    copy //= 10
  if n == rev:
    print("It's a palindrome number.")
  else:
    print("It's NOT a palindrome number.")
isPalindrome(131)