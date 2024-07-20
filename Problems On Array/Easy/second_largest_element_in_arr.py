
# Brute Force Approach

def second_largest(arr, n):
  arr.sort()
  return arr[n-2]

arr = [12, 1234, 45, 67, 1]
n = len(arr)
Ans1 = second_largest(arr, n)
print("Second largest element is:", Ans1)


def second_smallest(arr, n):
  arr.sort()
  return arr[1]

arr = [12, 1234, 45, 67, 1]
n = len(arr)
Ans2 = second_smallest(arr, n)
print("Second smallest element is:", Ans2)

#------------------------------------------------

# Better Solution

def second_largest_n_smallest(arr, n):
  if n == 0 or n == 1:
    return (-1, -1)

  small = float("inf")
  sec_small = float("inf")
  large = float("-inf")
  sec_large = float("-inf")

  for i in range(n):
    small = min(small, arr[i])
    large = max(large, arr[i])

  for i in range(n):
    if arr[i] < sec_small and arr[i] != small:
      sec_small = arr[i]
    if arr[i] > sec_large and arr[i] != large:
      sec_large = arr[i]

  return (sec_small, sec_large)


arr = [12, 1234, 45, 67, 1]
n = len(arr)
Ans = second_largest_n_smallest(arr, n)
print("Second smallest & largest element is:", Ans)

#------------------------------------------------

# Optimal Solution 

def second_smallest(arr, n):
  small = float("inf")
  sec_small = float("inf")

  for i in range(n):
    if arr[i] < small:
      sec_small = small
      small = arr[i]
    elif arr[i] < sec_small and arr[i] != small:
      sec_small = arr[i]

  return sec_small

def second_largest(arr, n):
  large = float("-inf")
  sec_large = float("-inf")

  for i in range(n):
    if arr[i] > large:
      sec_large = large
      large = arr[i]
    elif arr[i] > sec_large and arr[i] != large:
      sec_large = arr[i]

  return sec_large

arr = [12, 1234, 45, 67, 1]
n = len(arr)
Ans1 = second_smallest(arr, n)
Ans2 = second_largest(arr, n)
print("Second smallest element is:", Ans1)
print("Second largest element is:", Ans2)



