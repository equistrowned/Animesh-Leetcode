class Solution:
    def reverse(self, x: int) -> int:
        sx = str(x)
        if sx[0] == "-":
            res = sx[:0:-1]
            resfnl = int(res)* -1
        else:
            resfnl = int(sx[::-1])

        if resfnl < (-2) ** 31 or resfnl > (2**31) -1:
            return 0
        else:
            return resfnl