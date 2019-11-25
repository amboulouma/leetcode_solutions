# O(n) time
# O(1) space
# Dynamic approach

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        elif n==1: return 1
        elif n==2: return 2
        else: 
            temp_1, temp_2 = 1, 2
            output = 3
            for i in range(2, n):
                output = temp_1 + temp_2
                temp_1 = temp_2
                temp_2 = output
            return output