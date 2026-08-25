class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for x in range(0, n):
            if 3**x > n:
                break
            if n == 3 ** x:
                return True
        return False
