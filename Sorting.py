def selection_sort( arr, n ):
  for i in range(0, n):
    mini = i
    for j in range(i+1, n):
      if arr[j] < arr[mini]:
        mini = j
    arr[i], arr[mini] = arr[mini], arr[i]
    
#----------------Bubble Sort ----------------------------
def bubble_sort( arr, n ):
  for i in range(n):
    didSwap = 0
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        didSwap += 1
    if didSwap == 0:
      break
    
def insertion_sort( arr, n ):
  for i in range(n):
    j = i
    while( j>0 and arr[j-1] > arr[j] ):
      arr[j-1], arr[j] = arr[j], arr[j-1]
      j -= 1

def mergeSort( arr, low, high ):
  if low >= high:
    return
  mid = (low + high)//2
  mergeSort( arr, low, mid )
  mergeSort( arr, mid+1, high )
  merge( arr, low, mid, high )

def merge( arr, low, mid, high):
  left = low
  right = mid+1
  temp = []
  
  while(left <= mid and right <= high):
    if(arr[left] <= arr[right]):
      temp.append(arr[left])
      left += 1
    else:
      temp.append(arr[right])
      right += 1

  while(left <= mid):
    temp.append(arr[left])
    left += 1
    
  while(right <= high):
    temp.append(arr[right])
    right += 1
  
  for i in range(low, high+1):
    arr[i] = temp[i - low]


if __name__ == '__main__' :
  arr = [2, 9, 4, 18, 6]
  n = len(arr)
  print("Original Array:", arr)
  #selction_sort( arr, n )
  #bubble_sort( arr, n )
  #insertion_sort( arr, n )
  #mergeSort(arr, 0, n-1)
  print("Sorted:", arr) #[2, 4, 6, 9, 18] 
  
  
  
  
