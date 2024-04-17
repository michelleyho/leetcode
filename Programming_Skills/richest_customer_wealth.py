# 1672 Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_seen = 0
        for account in accounts:
            max_seen = max(max_seen, sum(account))
        
        return max_seen
