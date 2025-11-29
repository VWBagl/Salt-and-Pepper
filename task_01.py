import re

def is_palindrome(string):

    new_s = re.sub(r'[^a-zA-Z0-9]', '', string)
    new_s = new_s.lower()
    left = 0
    right = len(new_s)-1

    while left < right:
        if new_s[left] != new_s[right]:
            return False

        left += 1
        right -= 1
        
    return True