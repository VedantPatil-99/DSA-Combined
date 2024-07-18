# Function to check if a string is a palindrome using recursion
def isPalindrome(s, i):
    if i >= len(s) // 2:
        return True
    if s[i] != s[len(s) - i - 1]:
        return False
    return isPalindrome(s, i + 1)

s = input("Enter a string: ")
if isPalindrome(s, 0):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is NOT a palindrome.")

# s = "RADAR"
# RADAR is a palindrome.