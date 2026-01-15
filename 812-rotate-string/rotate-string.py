class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # def shift(s):
        #     for i in s:
        #         idx = s.index(i) + 1
        #         idx = idx % max(idx)
        #     print(idx)

        ### Correct Approach 1
        # ls = []
        # for i in range(len(s)):
        #     first = s[0:(len(s)-1)]
        #     last = s[-1]
        #     s = last + first
        #     ls.append(s)
        # if goal in ls:
        #     return True
        # else:
        #     return False



        for i in range(len(s)):
            if s == goal:
                return True
            s = s[-1] + s[:-1]
        return False


        
