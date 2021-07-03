
def isPalindrome(s):
    left = 0
    right = len(s)-1  
    
    #want to makes sure the left and right charaters are letters then check if they are the same if so then procced if not the false
    while left < right:
        if s[left].isalnum() == False:
            left += 1
            continue
        if s[right].isalnum() == False:
            right -= 1
            continue
    #after checing if they are letters chech if the left and the right are the same
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True

print(isPalindrome("race a car"))