class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        dp = [[1]]

        for i in range(1, numRows):
            prev = dp[-1]
            row = [1]

            for j in range(1, i):
                row.append(prev[j-1]+prev[j])

            row.append(1)
            dp.append(row)
        return dp

        