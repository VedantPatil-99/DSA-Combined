def armstrong_number(n):
  sum = 0
  power = len(str(n))
  copy = n
  while copy > 0:
    digit = copy % 10
    sum += (digit ** power)
    copy //= 10
  if n == sum:
    print("It's a armstrong number.")
  else:
    print("It's NOT a armstrong number.")
armstrong_number(370)

  