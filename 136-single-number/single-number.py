class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

        for key, value in count.items():
            if value == 1:
                return key

        # nums.sort()
        # for i in range(0, len(nums)-1, 2):
        #     if nums[i] != nums[i+1]:
        #         return nums[i]
        # return nums[-1]



