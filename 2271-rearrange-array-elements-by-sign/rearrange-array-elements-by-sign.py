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
        p = 0
        n = 0

        while p < len(pos):
            res.append(pos[p])
            res.append(neg[n])
            p += 1
            n += 1

        return res

        
