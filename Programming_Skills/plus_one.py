# 66 Plus One
# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reverse_digits = digits[::-1]
        carry = 1
        for i, v in enumerate(reverse_digits):
            new_sum = v + carry
            reverse_digits[i] = new_sum % 10
            carry = new_sum // 10
            
        if carry:
            reverse_digits.append(carry)
        
        return reverse_digits[::-1]

