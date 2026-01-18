class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1 = sorted(nums1)

        n=len(nums1)
        # if len(nums1) <= 1:
        #     median = nums1[0]

        if len(nums1) % 2 != 0:
            median = nums1[n//2]
        
        else:
            median = (nums1[n//2 -1] + nums1[n//2]) / 2
        return median