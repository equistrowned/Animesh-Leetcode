class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # return set(nums)
        for i in range(len(nums)):
            j=i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                else:
                    j += 1
        return len(nums)
