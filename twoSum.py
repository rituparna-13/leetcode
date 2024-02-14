# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Use a dictionary numsToindex to save the list elements
            with an index for faster access later. 
            To find the second index we can check this dictionary and
            retrive the index if the target is present.
            Time complexity: O(nlogn)
        '''
        numsToindex = {}
        for i in range(len(nums)):
            if target - nums[i] in numsToindex:
                return [numsToindex[target - nums[i]],i]
            else:
                numsToindex[nums[i]] = i
        return []
