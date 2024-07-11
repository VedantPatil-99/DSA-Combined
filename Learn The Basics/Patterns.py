#------------------- Square Pattern -------------------------
def square_pattern(n):
    """
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    """
    for i in range(n):
        print("* " * n)

#----------------- Right Triangle Pattern -------------------
def right_triangle_pattern(n):
    """
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
    """
    for i in range(n):
        print("* " * (i + 1))

#------------------- Number Triangle ------------------------
def number_triangle(n):
    """
    1
    12
    123
    1234
    12345
    """
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end="")
        print()

#------------------ Repeated Number Triangle ----------------
def repeated_number_triangle(n):
    """
    1
    22
    333
    4444
    55555
    """
    for i in range(n):
        print(str(i + 1) * (i + 1))

if __name__ == '__main__':
    n = 5
    
    print("Square Pattern:")
    square_pattern(n)
    
    print("\nRight Triangle Pattern:")
    right_triangle_pattern(n)
    
    print("\nNumber Triangle:")
    number_triangle(n)
    
    print("\nRepeated Number Triangle:")
    repeated_number_triangle(n)