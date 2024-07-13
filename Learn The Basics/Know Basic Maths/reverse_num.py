def reverse_number(n):
  rev = 0
  while n > 0:
    digit = n % 10
    rev = (rev * 10) + digit
    n //= 10
  return rev
print("Reversed:", reverse_number(754))
  