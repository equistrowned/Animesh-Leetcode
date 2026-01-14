class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # mp = min(prices)
        # mpi = prices.index(mp)
        # l2 = []
        # for i in range(mpi+1, len(prices)):
        #     l2.append(prices[i])
        # if not l2:
        #     return 0
        # # print(l2)
        # mx = max(l2)
        # # print(mx)
        # res = mx-mp
        # return max(0, res)

        mp = prices[0]
        mpr = 0
        for i in range(1, len(prices)):
            if prices[i] >mp:
                mpr = max(mpr, prices[i] - mp)
            else:
                mp = prices[i]

        return mpr


        

