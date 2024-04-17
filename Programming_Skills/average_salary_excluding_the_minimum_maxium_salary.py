# 1491 Average Salary Excluding the Minimum and Maximum Salary
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)-min(salary)-max(salary)
        return total/(len(salary)-2)
