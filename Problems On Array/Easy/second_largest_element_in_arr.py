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

