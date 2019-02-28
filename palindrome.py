# This is Python 2
import sys
#Read in input
line = raw_input()

#Use this variable to track whether or not the given input is a palindrome
isPalindrome = None


#Your code should be here (set isPalindrome to True or False)
# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return isPalindrome
    return False


#Returns true or false based on isPalindrome
if isPalindrome:
    print 'true'
else:
    print 'false'
