class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #inplace
        for i in range(len(nums1)):
            if nums1[i] == 0 and nums2:
                nums1[i] = nums2[0]
                nums2.pop(0)
    #sorting
        for j in range(len(nums1)):
            for k in range(j, len(nums1)):
                if nums1[j] > nums1[k]:
                    nums1[j], nums1[k] = nums1[k], nums1[j]