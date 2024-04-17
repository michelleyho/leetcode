# 283 Move Zeros
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for num in nums:
            if num != 0:
                nums[left] = num
                left += 1
        
        while left < len(nums):
            nums[left] = 0
            left += 1
        
        
        return nums
