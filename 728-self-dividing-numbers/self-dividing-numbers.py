class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res=[]
        def selfdiv(num):
            original = num
            dig = []

            while num >= 10:
                d = num % 10
                dig.append(d)
                num = num // 10

            dig.append(num)

            for di in dig:
                if di == 0:
                    return False

                if original % di != 0:
                    return False

            return True


        for i in range(left, right + 1, 1):
            if selfdiv(i):
                res.append(i)
        return res
        