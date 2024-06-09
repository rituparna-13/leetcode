# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    # Input: Two sorted integer lists.
    # Output: median of the lists.
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the sorted lists
        mergedArr = sorted(nums1 + nums2)
        # Save length (len) of the merged array
        mergedArr_len = len(mergedArr)
        # For even median will be (len/2 + (len/2 - 1)) / 2.
        if len(mergedArr) % 2 == 0:
            median = (mergedArr[int(mergedArr_len/2)] + mergedArr[int(mergedArr_len/2) - 1]) / 2
            return median
        else:
            # For odd median will be len / 2
            median = mergedArr[int(mergedArr_len/2)]
            return median
        
