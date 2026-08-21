class Solution:
    def isPalindrome(self, s: str) -> bool:
        resStr= ''
        
        for c in s:
            if c.isalnum():
                resStr += c.lower()
        return (resStr == resStr[::-1])        
        