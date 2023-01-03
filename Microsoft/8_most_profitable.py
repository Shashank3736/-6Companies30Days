# Leetcode 2467: Most Profitable Path in a Tree
# https://leetcode.com/problems/most-profitable-path-in-a-tree/
from math import inf
class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n = len(edges) + 1
        graph = {}
        for i,j in edges:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            graph[i].append(j)
            graph[j].append(i)
        seen = [0] * n

        def dfs(i, d0):
            seen[i] = 1
            res = -inf
            db = 0 if i == bob else n
            for j in graph[i]:
                if seen[j]: continue
                cur, kk = dfs(j, d0 + 1)
                res = max(res, cur)
                db = min(db, kk)
            if res == -inf: res = 0
            if d0 == db: res += amount[i] // 2
            if d0 < db: res += amount[i]
            return res, db + 1

        return dfs(0, 0)[0]

if __name__ == "__main__":
    s = Solution()
    print(s.mostProfitablePath([[0,1], [1,2], [1,3], [3, 4]], 3, [-2,4,2,-4,6])) # 6