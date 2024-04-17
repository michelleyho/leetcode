# 1502 Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val, max_val = min(arr), max(arr)
        if min_val == max_val:
            return True
        
        if (max_val-min_val) % (len(arr)-1) != 0:
            return False
            
        delta = (max_val - min_val)//(len(arr)-1)
        
        candidate = set()
        for num in arr:
            if (num-min_val) % delta != 0:
                return False
            
            candidate.add(num)
        
        return len(candidate) == len(arr)
                    
