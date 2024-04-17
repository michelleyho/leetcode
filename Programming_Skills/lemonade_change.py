# 860 Lemonade Change
# https://leetcode.com/problems/lemonade-change
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_freq = [0,0]
        
        for b in bills:
            
            if b == 5:
                bill_freq[0] += 1
            elif b == 10:
                if bill_freq[0] == 0:
                    return False
                bill_freq[0] -= 1
                bill_freq[1] += 1
            else:
                if bill_freq[1] > 0 and bill_freq[0] > 0:
                    bill_freq[1] -= 1
                    bill_freq[0] -= 1
                elif bill_freq[0] > 2:
                    bill_freq[0] -= 3
                else:
                    return False
        return True
