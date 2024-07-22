def left_rotate_one(arr, n):
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    for i in range(n):
        print(temp[i], end=" ")
    print()

n = 5
arr = [1, 2, 3, 4, 5]
left_rotate_one(arr, n)

