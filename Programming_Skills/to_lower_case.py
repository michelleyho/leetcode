# 709 To Lower Case
# https://leetcode.com/problems/to-lower-case
class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join([l.lower() for l in s])
