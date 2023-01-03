# Leetcode 581: Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int: 
        n = len(nums)
        if n == 1:
            return 0
        left = 0
        right = n - 1
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        subarray = nums[left:right + 1]
        min_num = min(subarray)
        max_num = max(subarray)
        while left > 0 and nums[left - 1] > min_num:
            left -= 1
        while right < n - 1 and nums[right + 1] < max_num:
            right += 1
        return right - left + 1

if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))