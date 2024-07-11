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
        
#----------------- downward_triangle_of_asterisks -------------------------
def downward_triangle_of_asterisks(n):
    """
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    for i in range(n, 0, -1):
        print("* " * i)

#----------------- downward_triangle_of_numbers -------------------------
def downward_triangle_of_numbers(n):
    """
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    """
    for i in range(n, 0, -1):
        print(" ".join(str(j) for j in range(1, i+1)))

#----------------- pyramid_of_asterisks -------------------------
def pyramid_of_asterisks(n):
    """
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
    """
    for i in range(0, n):
        for j in range(n-i-1):
            print(" ", end=" ")
        for j in range(2*i + 1):
            print("* ", end="")
        for j in range(n-i-1):
            print(" ", end=" ")
        print()

#----------------- upside_down_pyramid_of_asterisks -------------------------
def upside_down_pyramid_of_asterisks(n):
    """
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
    """
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(2*n - (2*i + 1)):
            print("* ", end="")
        for j in range(i):
            print(" ", end=" ")
        print()

#----------------- diamond_shape_of_asterisks -------------------------
def diamond_shape_of_asterisks(n):
    """
    Output:
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
    """
    pyramid_of_asterisks(n)
    upside_down_pyramid_of_asterisks(n)




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
    
    print("\nDownward Triangle of Asterisks:")
    downward_triangle_of_asterisks(n)
    
    print("\nDownward Triangle of Numbers:")
    downward_triangle_of_numbers(n)
    
    print("\nPyramid of Asterisks:")
    pyramid_of_asterisks(n)
    
    print("\nUpside-Down Pyramid of Asterisks:")
    upside_down_pyramid_of_asterisks(n)
    
    print("\nCombined Patterns 3 and 4 (Diamond Shape):")
    diamond_shape_of_asterisks(n)
    
    