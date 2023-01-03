# Leetcode 2344: Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
import math
class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i]= 1
            else:
                d[i]+=1

        nums[:] = list(d.keys())
        nums.sort()
        cnt = 0

        def GcdOfArray(arr, idx):
            if idx == len(arr)-1:
                return arr[idx]

            a = arr[idx]
            b = GcdOfArray(arr,idx+1)

            return math.gcd(a, b)
        gcd = GcdOfArray(numsDivide,0)
        ans = 0
        for ele in nums:
            if gcd%ele==0:
                ans = ele
                break
            else:
                cnt+=d[ele]
        if ans==0:
            return -1
        else:
            return cnt

if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([2, 3, 2, 4, 3], [9, 6, 9, 3, 15]))
    print(s.minOperations([4, 3, 6], [8, 2, 6, 10]))