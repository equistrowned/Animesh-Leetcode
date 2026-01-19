class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        res2 = []
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        asc = dict(sorted(count.items(), key=lambda item: item[1]))
        desc = dict(reversed(list(asc.items())))
        
        for key in desc.keys():
            res.append(key)
        for i in range(k):
            res2.append(res[i])
        return res2