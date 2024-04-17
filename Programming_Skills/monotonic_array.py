# 896 Monotonic Array
# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            if nums[i] < nums[i-1]:
                increasing = False  
        
        return increasing or decreasing
            
