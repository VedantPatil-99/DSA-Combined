# Brute Force Approach 
def isSorted_1(arr, n):
  for i in range(n):
    for j in range(i+1, n):
      if arr[j] < arr[i]:
        return False
    return True

arr1 = [12, 1234, 45, 67, 1]
n1 = len(arr1)
Ans1 = isSorted_1(arr1, n1)
print("Is Array Sorted?:", Ans1)

# Optimal Solution 

def isSorted_2(arr, n):
  for i in range(1, n):
    if arr[i] < arr[i-1]:
      return False
  return True

arr2 = [12, 1234, 45, 67, 1]
arr2.sort()
n2 = len(arr2)
Ans2 = isSorted_2(arr2, n2)
print("Is Array Sorted?:", Ans2)