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




# Brute Force Approach

from typing import List
def remove_duplicates_1(arr: List[int], n) -> int:
  if n == 0:
    return 0
  st = set()
  for i in range(n):
    st.add(arr3[i])
  k = len(st)
  j = 0
  for x in st:
    arr[j] = x
    j += 1
  return k

arr3 = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8]
n3 = len(arr3)
Ans3 = remove_duplicates_1(arr3, n3)
print("Array after removing duplicates:", arr3[:Ans3])



# Optimal Solution

def remove_duplicates_1(arr, n):
  i = 0
  for j in range(1, n):
    if arr[i] != arr[j]:
      i += 1
      arr[i] = arr[j]
  return i+1

arr4 = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8]
n4 = len(arr4)
Ans4 = remove_duplicates_1(arr4, n4)
print("Array after removing duplicates:", arr4[:Ans4])