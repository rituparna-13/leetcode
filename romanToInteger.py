# Given a roman numeral, convert it to an integer.

class Solution:
    # Input: Roman numeral as string.
    # Output: Return the integer value of the string.
    def romanToInt(self, s: str) -> int:
        ''' Time complexity: O(n) where n is the length of the string s. '''
        # From the problem statement first saved the Roman numeral to their respective integer values.
        # Use this dictionary to fetch the respective interger values of the Roman numerals.
        romanDict_singles = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        romanDict_double = {"IV":4, "IX":9, "XL":40, "XC":90, "CD": 400, "CM": 900}
        result = 0
        checkedIndex = []
        for i in range(len(s)):
            if i in checkedIndex:
                continue
            # First check for exceptional Roman numerals where two characters from s should be considered.
            if i+1 < len(s) and s[i]+s[i+1] in romanDict_double:
                print(s[i]," ",s[i+1])
                result = result + romanDict_double[s[i]+s[i+1]]
                checkedIndex.append(i+1)
            else:
                result = result + romanDict_singles[s[i]]
        return result
        
