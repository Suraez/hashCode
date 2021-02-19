from math import floor
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        if len(nums1) == 1 and len(nums2) == 0:
            return float(nums1[0])
        elif len(nums2) == 1 and len(nums1) == 0:
            return float(nums2[0])
        elif len(nums1) == 0 and len(nums2) == 0:
            return 0.00
        else:
            nums1.extend(nums2)
            nums1.sort()
            if len(nums1)%2 == 0:
                i1 = int(len(nums1)/2) -1
                i2 = int(len(nums1)/2)
                return float((nums1[i1] + nums1[i2]) / 2)
            else:
                return float(nums1[floor(len(nums1)/2)])

s = Solution()
print(s.findMedianSortedArrays([1,2],[3]))