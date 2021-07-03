def isPalindrome(s):
        i = 0
        j = len(s) - 1
        while (i < j):
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

def longestPalindrome(s):
        #The result is the largest paldrome taken from the substring with a list comprehention
        result = ""
        #With a double loop we go from the decreasing from the left to the right. ie. 11111 -> 01111...->00001
        #the secound loop linceases to the right with ever iteration ie. 10000->11000->
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                #this checks if it is Palindrome and is bigger then the already stored
                if j - i > len(result) and isPalindrome(s[i:j+1]):
                    #this changes the results of the code if it is larger
                    result = s[i:j+1]
        return result

print(isPalindrome("racecar"))
print(longestPalindrome("cbbd"))
