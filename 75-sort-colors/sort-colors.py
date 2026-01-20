class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        times = len(nums)

        for _ in range(times):
            l = 0
            r = 1

            while r < times:
                if nums[l] > nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1