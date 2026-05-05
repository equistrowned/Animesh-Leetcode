class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        opon = []
        for j in range(1,n+1):
            opon.append(j)


        def combi():
            fnl = []
            l = len(opon)
            res,sol = [],[]
        

            def backtrack(i):
                if i == l:
                    res.append(sol[:])
                    return

                #dont choose
                backtrack(i+1)

                #choose
                sol.append(opon[i])
                backtrack(i+1)
                sol.pop()

            backtrack(0)
            for r in res:
                if len(r) == k:
                    fnl.append(r)
            return fnl
        return combi()
                