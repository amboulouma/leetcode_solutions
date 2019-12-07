# Naive solution
# O(n²) Time
# O(1) Space
class Solution1:
    def lengthOfLongestSubstring(self, s):
        atomic_string, ans = "", 0
        for i,c in enumerate(s):
            if c in atomic_string: 
                s_ = s[i - len(atomic_string) :i]
                atomic_string = s_[s_.index(c) + 1:] + c
            else: atomic_string += c
            ans = max(ans, len(atomic_string))
        return ans

# Sliding windows solution
# O(2n) time
# O(1) space
class Solution2:
    def lengthOfLongestSubstring(self, s):
        n, set_, ans, i, j = len(s), set(), 0, 0, 0
        while i < n and j < n:
            if not (s[j] in set_) :  
                set_.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                set_.remove(s[i])
                i += 1 
        return ans

# Sliding windows optimized solution
# O(n) time
# O(1) space
class Solution3:
    def lengthOfLongestSubstring(self, s):
        n, index, ans, i, j = len(s), [0]*128, 0, 0, 0
        while j < n:
            i = max(index[ord(s[j])], i)
            ans = max(ans, j - i + 1)
            index[ord(s[j])] = j + 1
            j += 1
        return ans

s = Solution3()
print(s.lengthOfLongestSubstring("abcabcdbb"))