class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        res = ""
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        asc = dict(sorted(count.items(), key=lambda item: item[1]))
        desc = dict(reversed(list(asc.items())))
        
        # return desc

        for key, value in desc.items():
            while value > 0:
                res += "".join(key)
                value -= 1
        return res
