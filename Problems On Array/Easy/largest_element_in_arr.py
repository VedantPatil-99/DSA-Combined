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

#----------------------------------------------

#Recursive Approach 

def largest_element(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

def smallest_element(arr, n):
    min = arr[0]
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    return min

arr = [12, 1234, 45, 67, 1]
n = len(arr)
Ans1 = largest_element(arr, n)
Ans2 = smallest_element(arr, n)
print("Largest in given array is", Ans1)
print("Smallest in given array is", Ans2)

