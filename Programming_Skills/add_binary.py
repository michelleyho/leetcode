# 67 Add Binary
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(a, b, c):
            total = a + b + c
            return total % 2, total // 2
        
        result = []
        carry = 0
        a_ptr, b_ptr = len(a)-1, len(b)-1
        while a_ptr >=0 or b_ptr >=0 :
            a_val = int(a[a_ptr]) if a_ptr >= 0 else 0
            b_val = int(b[b_ptr]) if b_ptr >= 0 else 0
            digit, carry = add(a_val, b_val, carry)
            result.append(digit)
            if a_ptr >= 0: 
                a_ptr -= 1
            if b_ptr >= 0: 
                b_ptr -= 1
            
        if carry:
            result.append(carry)
            
        return ''.join([str(digit) for digit in result[::-1]])
