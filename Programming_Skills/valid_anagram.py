# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram
'''
Time: O(n) where worse case N is length of s or t.  
Need to build freq_map, as well as loop through s or t

Space: O(n) --> O(26) --> lowercase english letters (constant)
could use array of len 26
but unicode (can be more than 1 million characters)

Is Unicode limited to 128 characters?
The standard, which is maintained by the Unicode Consortium, defines as of the current version (15.0) 149,186 characters covering 161 modern and historic scripts, as well as symbols, 3664 emoji (including in colors), and non-visual control and formatting codes.

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = Counter(s)
        
        for letter in t:
            if letter not in s_freq:
                return False
            s_freq[letter] -= 1
            if s_freq[letter] == 0:
                del s_freq[letter]
        
        #return True # s=ab, t=a
        return not s_freq
