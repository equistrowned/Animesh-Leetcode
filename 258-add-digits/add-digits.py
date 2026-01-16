class Solution:
    def addDigits(self, num: int) -> int:

        def sm(n: int):
            s = 0
            ln = []
            sn = str(n)
            for i in sn:
                ln.append(int(i))
            smm = sum(ln)
            if smm < 10:
                return smm
            else:
                return sm(smm)
                

        return sm(num)
