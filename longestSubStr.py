# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    # Input: string s.
    # Output: length of the longest substring without repeating characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
       ''' Time complexity O(n) '''
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0 # use two pointers and sliding window concept.

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxLength
            
        
