import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = []
        heapq.heapify(nums)
        while nums:
            l.append(heapq.heappop(nums))
        # print(l)
        lr = l[::-1]

        return lr[k-1]