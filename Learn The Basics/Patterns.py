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
    
#----------------- star_pattern -------------------------
def star_pattern(n):
    """
    Output:
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    """
    for i in range(1, 2*n):
        stars = i
        if i > n:
            for j in range(2*n - i):
                print("*", end="")
        else:
            for j in range(stars):
                print("*", end="")
        print()

#----------------- Alternating 0 and 1 Pattern -------------------------
def alternating_binary_pattern(n):
    """
    1
    01
    101
    0101
    10101
    """
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(start, end="")
            start = 1 - start
        print()

#----------------- Number Pyramid with Spaces -------------------------
def number_pyramid_with_spaces(n):
    """
    1                 1
    1 2             2 1
    1 2 3         3 2 1
    1 2 3 4     4 3 2 1
    1 2 3 4 5 5 4 3 2 1
    """
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(1, (2 * (n - i) + 1)):
            print(" ", end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

#----------------- Incremental Number Triangle -------------------------
def incremental_number_triangle(n):
    """
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    """
    num = 1
    for i in range(n):
        for j in range(i + 1):
            print(num, end=" ")
            num += 1
        print()

#----------------- Incremental Alphabet Triangle -------------------------
def incremental_alphabet_triangle(n):
    """
    A
    B C
    D E F
    G H I J
    K L M N O
    """
    alpha = ord('A')
    for i in range(n):
        for j in range(i + 1):
            print(chr(alpha), end=" ")
            alpha += 1
        print()

#----------------- Alphabet Triangle -------------------------
def alphabet_triangle(n):
    """
    A
    A B
    A B C
    A B C D
    A B C D E
    """
    for i in range(n):
        alphabet = ord('A')
        for j in range(i + 1):
            print(chr(alphabet), end=" ")
            alphabet += 1
        print()

#----------------- Reverse Alphabet Triangle -------------------------
def reverse_alphabet_triangle(n):
    """
    A B C D E
    A B C D
    A B C
    A B
    A
    """
    for i in range(n, 0, -1):
        alphabet = ord('A')
        for j in range(i):
            print(chr(alphabet), end=" ")
            alphabet += 1
        print()

#----------------- Repeated Alphabet Triangle -------------------------
def repeated_alphabet_triangle(n):
    """
    A
    B B
    C C C
    D D D D
    E E E E E
    """
    letter = ord('A')
    for i in range(n):
        for j in range(i + 1):
            print(chr(letter), end=" ")
        letter += 1
        print()


#----------------- Pyramid of Alphabets -------------------------
def pyramid_of_alphabets(n):
    """
         A         
       A B A       
     A B C B A     
   A B C D C B A   
 A B C D E D C B A 
    """
    for i in range(n):
        alpha = ord('A')
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(i + 1):
            print(chr(alpha + j), end=" ")
        for j in range(i):
            print(chr(alpha + i - j - 1), end=" ")
        for j in range(n - i - 1):
            print(" ", end=" ")
        print()

#----------------- Reverse Alphabet Triangle -------------------------
def reverse_alphabet_triangle(n):
    """
    E
    D E
    C D E
    B C D E
    A B C D E
    """
    for i in range(n):
        alpha = ord('A')
        for j in range(i + 1):
            print(chr(alpha + n - i + j - 1), end="")
        print()

#----------------- Hourglass with Stars -------------------------
def hourglass_with_stars(n):
    """
    * * * * * * * * * * * *
    * * * * *     * * * * *
    * * * *         * * * *
    * * *             * * *
    * *                 * *
    *                     *
    * *                 * *
    * * *             * * *
    * * * *         * * * *
    * * * * *     * * * * *
    * * * * * * * * * * * *
    """
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        for j in range(2 * i):
            print(" ", end=" ")
        for j in range(n - i):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        for j in range(2 * (n - i - 1)):
            print(" ", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print()

#----------------- hollow_diamond_with_stars -------------------------
def hollow_diamond_with_stars(n):
    """
    *                 * 
    * *             * * 
    * * *         * * * 
    * * * *     * * * * 
    * * * * * * * * * * 
    * * * *     * * * * 
    * * *         * * * 
    * *             * * 
    *                 *                
    """
    for i in range(2 * n):
        if i >= n:
            for j in range(2 * n - i - 1):
                print("*", end=" ")
            for j in range((i - n) * 2 + 2):
                print(" ", end=" ")
            for j in range(2 * n - i - 1):
                print("*", end=" ")
        else:
            for j in range(i + 1):
                print("*", end=" ")
            for j in range(2 * (n - i - 1)):
                print(" ", end=" ")
            for j in range(i + 1):
                print("*", end=" ")
        print()
    


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
    
    print("Alternating 0 and 1 Pattern:")
    alternating_binary_pattern(n)
    
    print("\nNumber Pyramid with Spaces:")
    number_pyramid_with_spaces(n)
    
    print("\nIncremental Number Triangle:")
    incremental_number_triangle(n)
    
    print("\nIncremental Alphabet Triangle:")
    incremental_alphabet_triangle(n)
    
    print("\nAlphabet Triangle:")
    alphabet_triangle(n)
    
    print("\nReverse Alphabet Triangle:")
    reverse_alphabet_triangle(n)
    
    print("\nRepeated Alphabet Triangle:")
    repeated_alphabet_triangle(n)
    
    print("Pyramid of Alphabets:")
    pyramid_of_alphabets(n)
    
    print("\nReverse Alphabet Triangle:")
    reverse_alphabet_triangle(n)
    
    print("\nHourglass with Stars:")
    hourglass_with_stars(n)
    
    print("\nCombined Hourglass and Diamond with Stars:")
    hollow_diamond_with_stars(n)




