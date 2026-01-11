class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn, mx = min(nums), max(nums)
        gcd = 1

        if mx % mn == 0:
            return mn
        else:
            for i in range(1,mn+1):
                if mx%i == 0 and mn%i == 0:
                    gcd = i

            return gcd
                