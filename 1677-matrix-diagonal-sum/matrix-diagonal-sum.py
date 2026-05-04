class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        rows = len(mat)
        cols = len(mat[0])
        for i in range(cols):
            for j in range(rows):
                if i == j:
                    s = mat[i][j]
                    sum += s
                elif (i + j == rows-1 and i != j):
                    s = mat[i][j]
                    sum +=s

        return sum