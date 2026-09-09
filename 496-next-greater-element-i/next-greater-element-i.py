class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j]>nums1[i]:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res


