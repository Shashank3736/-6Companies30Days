# Leetcode 2344: Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
class Solution:
    def divideAllInList(self, nums: list[int], divisor: int) -> bool:
        for num in nums:
            if num % divisor != 0:
                return False
        return True
    
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        n = len(nums)
        res = 0

        while n > 0:
            if self.divideAllInList(numsDivide, min(nums)):
                break
            else:
                n -= 1
                res += 1
                # remove the lowest int from list nums
                nums.remove(min(nums))
        return res if n > 0 else -1  

if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([2, 3, 2, 4, 3], [9, 6, 9, 3, 15]))
    print(s.minOperations([4, 3, 6], [8, 2, 6, 10]))