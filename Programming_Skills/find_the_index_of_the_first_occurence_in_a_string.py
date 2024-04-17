#28 Find the index of the first occurrence in a string
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        ptr = 0
        left = 0
        
        while left <= (len(haystack)-needle_len):
            left_ptr = left
            while haystack[left_ptr] == needle[ptr]:
                left_ptr +=1
                ptr += 1
                if ptr == needle_len:
                    return left
            ptr = 0
            left += 1
        
        return -1
                
            
