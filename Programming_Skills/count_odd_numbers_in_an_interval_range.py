# 1523 Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = 0
        start, end = low, high
        if low %2 == 1:
            total += 1
            start += 1
        if high%2 == 1:
            total += 1
            end -= 1
        
        total += (end-start)//2
        
        return total

      
