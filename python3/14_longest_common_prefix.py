import functools 
import os

# O(n) time
# O(n) space

# Solution usins startwith
class Solution1:
    def longestCommonPrefix(self, strs) -> str:
        prefix = strs[0] if strs else ''
        while True:
            if all(s.startswith(prefix) for s in strs):
                return prefix
            prefix = prefix[:-1]

# Solution usins zip
class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        if strs: prefix = "" 
        else: return ''
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y: prefix += x
            else: break
        return prefix

# Using divide and conquer with reduce and list comprehension
class Solution3:
    def longestCommonPrefix(self, strs) -> str:
        if not strs: return ""
        return functools.reduce(self.merge, strs)

    def merge(self, h1, h2):
        i = 0
        while i < len(h1) and i < len(h2) and h1[i] == h2[i]: i += 1
        return h1[:i]

class Solution4:
    # python core library
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)

solution_3 = Solution3()
print(solution_3.longestCommonPrefix(["aaa","aa","aaa"]))