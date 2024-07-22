
# Brute Force Approach 

def left_rotate_one(arr, n):
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    for i in range(n):
        print(temp[i], end=" ")
    print()

arr1 = [1, 2, 3, 4, 5]
n1 = len(arr1)
left_rotate_one(arr1, n1)

#-------------------------------------

# Optimal Solution 

def left_rotate_one(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    for i in range(n):
        print(arr[i], end=" ")

arr2 = [1, 2, 3, 4, 5]
n2 = len(arr2)
left_rotate_one(arr2, n2)
