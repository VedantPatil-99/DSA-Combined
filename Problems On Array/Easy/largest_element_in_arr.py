# Brute force approach 

def largest_element1(arr, n):
  arr.sort()
  return arr[n-1]

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
print("Largest element is:", largest_element1(arr, n))


def smallest_element1(arr, n):
  arr.sort()
  return arr[0]

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
print("Smallest element is:", smallest_element1(arr, n))

#---------------------------------------