import functools

# Recursive approach with memoization
# O(n) time
# O(n) space
class Solution2:
    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else 2 if n == 2 else 1

# Dynamic approach with space optimization
# O(n) time
# O(1) space
class Solution1:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

# Mathematician formula
# O(log(n)) time to calculate the power by squarring
# O(1) space
class Solution3:
    def climbStairs(self, n: int) -> int:
        return int((5**.5 / 5) * (((1 + 5**.5)/2)**(n + 1) - ((1 - 5**.5)/2)**(n + 1)))