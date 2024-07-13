def count_digits(n):
  cnt = 0
  while(n > 0):
    lastdigit = n % 10
    n //= 10
    cnt += 1
  return cnt
digits = count_digits(1234)
print(digits)

def print_digits(n):
  while(n > 0):
    lastdigit = n % 10
    n //= 10
    print(lastdigit, end = " ")
print_digits(1234)