class Solution:
    def maximalSquare(self, matrix):
        n = len(matrix[1])


    def findsqure2(self,matrix,n):
        stack = [[0] * n-1] * n-1
        flag = False
        for i in range(n-1):
            for j in range(n-1):
                if matrix[i][j] == matrix[i+1][j] == matrix[i][j+1] == matrix[i+1][j+1] == 1:
                    stack[i][j] = 1
                    flag = True
        if flag:
            return stack
        else:
            return flag
