# Leetcode 216: Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, n, start, path, res):
            if k == 0 and n == 0:
                res.append(path)
                return
            for i in range(start, 10):
                helper(k - 1, n - i, i + 1, path + [i], res)
        res = []
        helper(k, n, 1, [], res)
        return res