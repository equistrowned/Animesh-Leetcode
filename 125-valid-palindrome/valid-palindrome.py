class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        alphs = "abcdefghijklmnopqrstuvwxyz0123456789"
        palchk = ""
        for _ in s:
            _ = _.lower()
            if _ in alphs:
                palchk += _
        # if len(palchk) <= 1:
        #     return False
        
        return palchk == palchk[::-1]
            