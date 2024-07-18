# Function to print numbers from 1 to N using recursion
def printUptoN(i, N):
    if i > N:
        return
    print(i, end=' ')
    printUptoN(i+1, N)

N = int(input("Enter the value of N: ")) # N = 10
printUptoN(1, N) # 1 2 3 4 5 6 7 8 9 10



# Function to print numbers from 1 to N using BACKTRACKING
def printUptoN(i, N):
    if i < 1:
        return
    printUptoN(i-1, N)
    print(i, end=' ')

N = int(input("Enter the value of N: ")) # N = 10
printUptoN(N, N) # 1 2 3 4 5 6 7 8 9 10



# Function to print numbers from N to 1 using recursion
def printFromN(i, N):
    if i < 1:
        return
    print(i, end=' ')
    printFromN(i-1, N)

N = int(input("Enter the value of N: ")) # N = 10
printFromN(N, N) # 10 9 8 7 6 5 4 3 2 1



# Function to print numbers from N to 1 using BACKTRACKING
def printFromN(i, N):
    if i > N:
        return
    printFromN(i+1, N)
    print(i, end=' ')

N = int(input("Enter the value of N: ")) # N = 10
printFromN(1, N) # 10 9 8 7 6 5 4 3 2 1