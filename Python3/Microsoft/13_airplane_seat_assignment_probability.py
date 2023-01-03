# Leetcode 1227: Airplane Seat Assignment Probability
# https://leetcode.com/problems/airplane-seat-assignment-probability/
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5

if __name__ == "__main__":
    s = Solution()
    print(s.nthPersonGetsNthSeat(1)) # 1.0
    print(s.nthPersonGetsNthSeat(2)) # 0.5