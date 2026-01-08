class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 1, x

        while l <= r:
            m = (l+r) // 2
            msq = m * m

            if msq == x:
                return m
            elif msq < x:
                l = m+1
            else:
                r = m-1
        return r
            
