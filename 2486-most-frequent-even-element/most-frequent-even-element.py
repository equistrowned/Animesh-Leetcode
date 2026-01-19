class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = {}
        # res = []
        # val = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] in count:
                count[nums[i]] += 1
            elif nums[i] % 2 == 0 and nums[i] not in count:
                count[nums[i]] = 1
        if count == {}:
            return -1
        seen = 0
        ans = None
        for key, value in count.items():
            if value > seen:
                seen = value
                ans = key
            elif value == seen and key < ans:
                ans = key
        return ans
            

 