# Leetcode 1392: Longest Happy Prefix
# https://leetcode.com/problems/longest-happy-prefix/
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return ''
        dp = [0] * n
        for i in range(1, n):
            j = dp[i - 1]
            while j > 0 and s[i] != s[j]:
                j = dp[j - 1]
            if s[i] == s[j]:
                j += 1
            dp[i] = j
        return s[:dp[n - 1]]

if __name__ == "__main__":
    s = Solution()
    print(s.longestPrefix('ababab'))
