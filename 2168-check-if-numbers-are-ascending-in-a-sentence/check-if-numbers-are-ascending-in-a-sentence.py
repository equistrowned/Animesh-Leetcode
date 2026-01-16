class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        # nums = '0123456789'
        # s = "".join(s.split())
        for i in s:
            if i in chars:
                s = s.replace(i, " ")
        arr = list(map(int, s.split()))
        for j in range(1, len(arr)):
            if arr[j] <= arr[j-1]:
                return False
        return True
        