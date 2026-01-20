class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #O(n^2) comp
        # times = len(nums)

        # for _ in range(times):
        #     l = 0
        #     r = 1

        #     while r < times:
        #         if nums[l] > nums[r]:
        #             nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r += 1

        nums2 = nums.copy()
        nums.clear()

        for i in range(len(nums2)):
            mn = min(nums2)
            nums.append(mn)
            nums2.remove(mn)

