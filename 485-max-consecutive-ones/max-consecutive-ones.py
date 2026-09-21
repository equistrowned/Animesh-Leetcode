class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxx = 0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxx=max(maxx,count)
                
            else:

                count =0
        
        return maxx
