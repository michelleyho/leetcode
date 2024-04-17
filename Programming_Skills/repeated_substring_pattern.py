#459. https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            curr_substr = s[:i]
            
            if len(s) % len(curr_substr) != 0:
                continue
            num_copies = len(s) // len(curr_substr)
            
            if curr_substr*num_copies == s:
                return True
        
        return False
                
