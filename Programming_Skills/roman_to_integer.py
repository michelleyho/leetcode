# 13 Roman to Integer
# https://leetcode.com/problems/roman-to-integer
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'M': 1000, 
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10, 
            'V': 5,
            'I': 1
            
        }
        total = 0
        i = 0
        while i < len(s):
            value = mapping[s[i]]
            if i+1 < len(s) and mapping[s[i+1]] > value:
                value = mapping[s[i+1]]-value
                i+= 1
            i+=1
            
            total += value
        
        return total
