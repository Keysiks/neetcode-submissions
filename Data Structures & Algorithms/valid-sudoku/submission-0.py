class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        def is_valid(nums):
            c = 0
            m = set()
            for i in range(len(nums)):
                if nums[i] != ".":
                    m.add(nums[i])
                    c += 1
            return c == len(m)

        for i in range(n):
            if not is_valid(board[i]):
                return False
        for i in range(n):
            m = set()
            c = 0
            for j in range(n):
                if board[j][i] != ".":
                    m.add(board[j][i])
                    c += 1
            if c != len(m):
                return False  

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                sp = [board[i][j + 1], board[i][j], board[i][j + 2],
                board[i + 1][j], board[i + 1][j + 1], board[i + 1][j + 2],
                board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]]
                if not is_valid(sp):
                    return False
        return True