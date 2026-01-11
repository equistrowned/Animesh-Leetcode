class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        divisors = 0
        flag = False

        for i in range(1, n+1):
            if n%i == 0:
                divisors += 1
        
            if divisors > 3:
                return False

        return divisors == 3