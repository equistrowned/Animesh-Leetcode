class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        asc = sorted(nums)
        # desc = asc.reverse()
        desc = asc[::-1]
        # print(asc)
        # print(desc)
        return nums == desc or nums == asc