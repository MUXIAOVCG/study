class Solution:
    def isValidSudoku(self, board) :
        judge = {"1": [[0]*9 for i in range(3)], "2": [[0]*9 for i in range(3)], "3": [[0]*9 for i in range(3)],
                 "4": [[0]*9 for i in range(3)], "5": [[0]*9 for i in range(3)], "6": [[0]*9 for i in range(3)],
                 "7": [[0]*9 for i in range(3)], "8": [[0]*9 for i in range(3)], "9": [[0]*9 for i in range(3)]
                 }
        print(judge)
        for i in range(9):
            for j in range(9):
                s = board[i][j]
                if s == '.':
                    continue
                if judge[s][0][i] + judge[s][1][j] \
                        + judge[s][2][(i//3)*3+j//3]:
                    return False
                else:
                    judge[s][0][i] = 1
                    judge[s][1][j] = 1
                    judge[s][2][(i//3)*3+j//3] = 1
        return True


obj = Solution()
print(obj.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
))