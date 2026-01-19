class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        s = len(nums)/2
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for key, value in count.items():
            if value > s:
                return key
        


        