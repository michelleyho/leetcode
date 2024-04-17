# 976 Largest perimeter triangle
# https://leetcode.com/problems/largest-perimeter-triangle

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter = 0
        for i in range(0, len(nums)-2):
            a, b, c = nums[i+2], nums[i+1], nums[i]
            if a+b > c:
                perimeter = max(perimeter, a+b+c)
        
        return perimeter
