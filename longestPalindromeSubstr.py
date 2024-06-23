''' Given a string s, return the longest palindromic substring in s.'''

class Solution:
    ''' Checks for palindrome by reversing the string. '''
    def isPalindrome(self, s):
        return s == s[::-1]

    ''' Checks for longest palindrome substring. '''
    def maxLen(self, sArr):
        max_len = -1
        result = sArr[0]
        for s in sArr:
            if len(s) > max_len:
                max_len = len(s)
                result = s
        return result

    def longestPalindrome(self, s: str) -> str:
        # Loop over the string to get substrings by changing start and end indices and check for palindrome.
        # Time complexity is O(n^2).
        palindrome_list = []
        for i in range(len(s)):
            substr = s[i]
            for j in range(i+1,len(s)):
                substr = substr + s[j]
                #print(substr)
                if self.isPalindrome(substr):
                    palindrome_list.append(substr)
        # This means that no substring is a palindrome but single characters are.
        if palindrome_list == []:
            return s[0]
        else:
            result = self.maxLen(palindrome_list)
            return result
        
