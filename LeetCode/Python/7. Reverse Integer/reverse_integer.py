class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        
        if x >= 0:
            a = int(str(x)[::-1])
        elif x < 0:
            a = -1 * int(str(abs(x))[::-1])
        
        if a >= 2**31-1 or a <= -2**31:
            return 0

        return a
