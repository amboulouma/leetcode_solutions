import functools

# Dynamic approach with space optimization
# O(n) time
# O(1) space
class Solution1:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

# Recursive approach with memoization
# O(n) time
# O(n) space
class Solution2:
    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else 2 if n == 2 else 1
