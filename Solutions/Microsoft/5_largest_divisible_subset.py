# Leetcode 368: Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_len = 0
        max_index = -1
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = prev[max_index]
        return res