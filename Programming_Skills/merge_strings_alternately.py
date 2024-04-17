# 1768 Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        result = []
        
        while ptr1 < len(word1) and ptr2 < len(word2):
            result.append(word1[ptr1])
            result.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1
        
        result.extend(word1[ptr1:])
        result.extend(word2[ptr2:])
        
        return ''.join(result)
        
