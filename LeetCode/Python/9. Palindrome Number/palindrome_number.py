class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            a = int(str(x)[::-1])
            if a == x:
                return True
            return False
        return False
