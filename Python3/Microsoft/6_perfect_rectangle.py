# Leetcode 391: Perfect Rectangle
# https://leetcode.com/problems/perfect-rectangle/
class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        if not rectangles:
            return False
        area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            corners ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
        if len(corners) != 4 or area != (max(x for x, y in corners) - min(x for x, y in corners)) * (max(y for x, y in corners) - min(y for x, y in corners)):
            return False
        return True