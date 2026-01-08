class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mx = max(nums)
        mn = min(nums)
        
        s = set(nums)
        l =[]

        for i in range(mn, mx+1):
            if i not in s:
                l.append(i)

        return l