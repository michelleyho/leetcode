# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = Counter(t)
        
        for ch in s:
            letters[ch] -= 1
            if letters[ch] == 0:
                del letters[ch]
        
        for k in letters.keys():
            return k
