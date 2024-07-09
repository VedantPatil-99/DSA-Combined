def selection_sort( arr, n ):
  for i in range(0, n):
    mini = i
    for j in range(i+1, n):
      if arr[j] < arr[mini]:
        mini = j
    arr[i], arr[mini] = arr[mini], arr[i]
    
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

if __name__ == '__main__' :
  arr = [2, 9, 4, 18, 6]
  print("Original Array:", arr)
  #selction_sort( arr, len(arr) )
  #bubble_sort( arr, len(arr) )
  insertion_sort( arr, len(arr) ) 
  print("Sorted:", arr) #[2, 4, 6, 9, 18] 
  
  
  
  
