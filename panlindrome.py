# The initial palindrome function had a few things that I did not like. First,
# all variable names were poorly chosen. I realize that is probably to test me,
# but nonetheless readable and self documenting code is pretty important. 
# Second, it has more for loops than I would deem necessary. The first for loop
# reverses the word and the second for loop compares each letter in the reversed
# the original. Meaning we have a big O of O(strLen) + O(strLen) or a total of O(strLen).
# But, in practice we are creating more work than needed for our program. I 
# created a solution that contains one for loop that iterates half of the string length.
# Third, I did not like that the original changed the iterator to True on every 
# successful pass. Past being somewhat useless until the very last pass, it also is bad
# practice to change an numerical iterator to a boolean. In my solution I instead 
# return False if it fails then, after loop is completed, True.

# Initial method.
def is_palindrone(s):
    r=""
    for c in s:
        r = c +r
    for x in range(0, len(s)):
        if s[x] == r[x]:
            x = True
        else:
            return False
    return x


# This method finds the center of the string and than compares
# each character of the string from the center out checking for
# equality. It will return True if it is indeed a palindrome, 
# false otherwise.
def is_palindromeModified(inputString):
    stringLength = len(inputString) - 1
    centerIndex = stringLength // 2
    even = stringLength % 2

    # loops through half of the string
    for i in range(0, centerIndex + 1):
        if inputString[centerIndex - i] != inputString[centerIndex + even + i]:
            return False

    return True
