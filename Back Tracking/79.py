class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(board, r, c, word, index):
            if index == len(word):      # 当最后一个找到的字母+1后和word长度相等，等同于到叶子节点，结束递归
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:    # 如果不满足条件，则return false
                return False
            board[r][c] = '*'       # 标记已经走过的位置，防止陷入来回跳的死循环
            up = dfs(board, r - 1, c, word, index + 1)      # 测试上面
            down = dfs(board, r + 1, c, word, index + 1)    # 测试下面
            left = dfs(board, r, c - 1, word, index + 1)    # 测试左
            right = dfs(board, r, c + 1, word, index + 1)   # 测试右
            res = up or down or left or right               # 有一个满足即可return true
            board[r][c] = word[index]                       # 回溯过程，标记回去走过的位置
            return res
        # 先找到第一个字母开始对应在Grid里面的位置
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(board, r, c, word, 0):       # 开始DFS搜索上下左右
                        return True
        return False
