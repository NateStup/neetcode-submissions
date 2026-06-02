import re

class Solution:
    def testPalindrome(self, s: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.testPalindrome(s, left + 1, right - 1)

    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        return self.testPalindrome(s, 0, len(s) - 1)