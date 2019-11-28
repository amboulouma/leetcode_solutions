# O(n) Time
# O(n) Space
# Python one liner
class Solution1:
    def searchInsert(self, nums, target: int) -> int:
        return len([x for x in nums if x<target])

# O(n) Time
# O(n) space
# Python core function
import bisect

class Solution2:
    def searchInsert(self, nums, target: int) -> int:
        return bisect.bisect_left(nums, target)

# O(n) time
# O(1) space
# Faster than 98.5% Python 3 submission
# Memory usage less than 100% submissions
class Solution3:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums: return nums.index(target)
        else:
            if nums and target > max(nums): return len(nums)
            if not nums : return 0
            for i, n in enumerate(nums): 
                if n > target: return i

# O(n) Time for sorting the array
# O(1) space
# Good use of the try except functionnality
class Solution4:
    def searchInsert(self, nums, target: int) -> int:
        try:
            return nums.index(target)
        except:
            nums.append(target)
            nums.sort()
        return nums.index(target)


# O(log(n)) Time
# O(1) space
# Binary search algorithm
class Solution5:
    def searchInsert(self, nums, target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: low = mid + 1
            else: high = mid - 1
        return low
