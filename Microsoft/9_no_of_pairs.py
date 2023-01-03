# Leetcode 2426: Number of Pairs Satisfying Inequality
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
from sortedcontainers import SortedList
import numpy as np

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        nums = np.array(nums1) - np.array(nums2)
        seen = SortedList()
        count = 0
        
        for n in nums:
            count += seen.bisect_right(n + diff)
            seen.add(n)
        
        return count