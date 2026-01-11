class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # return "".join(_ for _ in t if _ not in s)

        ls = list(s)
        lt = list(t)

        for i in ls:
            lt.remove(i)

        return lt[0]
