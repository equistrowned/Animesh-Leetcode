class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # def shift(s):
        #     for i in s:
        #         idx = s.index(i) + 1
        #         idx = idx % max(idx)
        #     print(idx)

        # sl = list(s)
        # for i in s:
        #     first = str(sl.remove(s[-1]))
        #     s = first + s
        #     if s == goal:
        #         return True
        #         break
        #     else:
        #         return False
        ls = []
        for i in range(len(s)):
            first = s[0:(len(s)-1)]
            last = s[-1]
            s = last + first
            ls.append(s)
        if goal in ls:
            return True
        else:
            return False


            # if s == goal:
            #     break
            #     return True
            # else:
            #     return False
            # print(s)


        
