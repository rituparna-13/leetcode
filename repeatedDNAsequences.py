# When studying DNA, it is useful to identify repeated sequences within the DNA.
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
# Can return the answer in any order.

class Solution:
    # Input: DNA sequence string.
    # Output: List of 10-letter-long sequences (substrings) that occur more than once in the DNA sequence string.
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ''' Time Complexity: O(n) where n is length of s. '''
        # List the 10-letter-long substrings of the string and then check if it appears more than once. If yes then add them to another list and return.
        result = set()
        subStr = set()
        for i in range(len(s)):
            # Constraint to not check for substrings less than length 10
            if (i+10 > len(s)):
                break
            # If the substring already exists then it should be added to result as it appears more than once
            if s[i:i+10] in subStr:
                result.add(s[i:i+10])
            else:
                subStr.add(s[i:i+10])
        return list(result)

            
        
