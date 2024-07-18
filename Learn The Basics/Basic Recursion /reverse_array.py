# Function to reverse an array using recursion
def reverse_arr(arr, start, end):
    if start > end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_arr(arr, start+1, end-1)

arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]
reverse_arr(arr, 0, len(arr)-1)
print(f"Reversed array: {arr}")

# arr = [1, 2, 3, 4, 5]
# Reversed array: [5, 4, 3, 2, 1]