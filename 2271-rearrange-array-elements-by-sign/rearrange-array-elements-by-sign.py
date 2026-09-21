class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=[]
        neg=[]
        res=[]
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        while len(pos)>0:
            res.append(pos.pop(0))
            res.append(neg.pop(0))
        return res

        
