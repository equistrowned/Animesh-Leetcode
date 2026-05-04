class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        l = []
        for i in range(cols):
            for j in range(rows):
                if i == j and grid[i][j] == 0:
                    return False
                elif (i + j == rows-1 and grid[i][j] == 0):
                    return False
                elif (i + j != rows -1 and i != j):
                    l.append(grid[i][j])
        # print(l)
        for p in range(len(l)):
            if l[p] != 0:
                return False

        return True
                    
                    

                    