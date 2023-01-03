# Leetcode 1358: Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        i = 0
        j = 0
        n = len(s)
        freq = [0] * 3
        while i < n:
            freq[ord(s[i]) - ord('a')] += 1
            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                freq[ord(s[j]) - ord('a')] -= 1
                j += 1
            count += j
            i += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSubstrings('abcabc')) # 10
    print(s.numberOfSubstrings('aaacb')) # 3
    print(s.numberOfSubstrings('abc')) # 1