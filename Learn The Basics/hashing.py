'''
What's Hashing? 
Given an array of integers: [1, 2, 1, 3, 2] and 
we are given some queries: [1, 3, 4, 2, 10]. 
For each query, we need to find out how many times the number appears in the array. 
For example, 
if the query is 1 our answer would be 2, and if the query is 4 the answer will be 0. 
'''
# Function to perform numerical hashing
def num_hashing(arr, queries):
    n = len(arr)
    hash = [0] * (max(arr) + 1)
    for num in arr:
        hash[num] += 1
    for query in queries:
        print(f"Count of {query}: {hash[query]}")
        
arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]
queries = [int(x) for x in input("Enter the query elements separated by space: ").split()]
num_hashing(arr, queries)

# Example Output-
'''
Enter the array elements separated by space: 1 2 3 5 6 3 2 2
Enter the query elements separated by space: 1 8 2

Count of 1: 1
Count of 8: 0
Count of 2: 3
'''

