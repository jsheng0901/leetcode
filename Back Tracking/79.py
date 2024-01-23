class Solution1:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def backtracking(self, board, r, c, word, index, m, n):
        # 回溯处理的是下一个节点，所以当找到最后一个的字母后+1后就和word长度相等，等同于找到一天到叶子节点合理的path，结束递归
        if index == len(word):
            return True

        # 如果当前节点不满足条件，则 return false
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
            return False

        # 标记已经走过的位置，防止陷入来回跳的死循环
        board[r][c] = "*"
        # 当前节点的子节点的返回值结果
        res = False
        for direction in self.directions:
            next_r = r + direction[0]
            next_c = c + direction[1]
            # 有一个满足即可 return true
            res = res or self.backtracking(board, next_r, next_c, word, index + 1, m, n)

        # 离开当前节点，回溯，标记回去走过的位置
        board[r][c] = word[index]

        return res

    def exist(self, board: [[str]], word: str) -> bool:
        """
        Time O(n * 3^l)
        Space O(l)
        回溯模板题，这里一定要记得离开当前节点的时候要撤回标记的操作，因为我们是要找合理的path，所以当前节点可能不能从上一个节点到，
        但是可以从别的节点过来，所以不能说visited一次后就一直不能再visited了。这是回溯题型和单纯的DFS最大的区别。
        时间复杂度上我们本质上是一个三叉树的节点遍历，所以最多3^l个节点，每个节点需要遍历一次board。
        """
        m = len(board)
        n = len(board[0])

        # 先找到第一个字母开始对应在 board 里面的位置
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    # 开始回溯搜索上下左右
                    if self.backtracking(board, r, c, word, 0, m, n):
                        return True
        return False


class Solution2:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(self, board, x, y, m, n, word, index):
        # 这里是一个区别，因为DFS进入递归的一定是合理的节点，所以不需要判断是否合理，同时DFS永远是判断当前节点，不是判断下一个节点
        # 当前节点等于等于最后一个词的时候说明找到合理的path，直接返回
        if index == len(word) - 1:
            return True

        # 标记当前节点访问过
        board[x][y] = "*"
        res = False
        for direction in self.directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            # 这里是另一个区别，下一个节点的判断防止进递归之前
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if board[next_x][next_y] != word[index + 1]:
                continue
            if board[next_x][next_y] == "*":
                continue
            # 可以进递归的都是合理的下一个节点
            res = res or self.dfs(board, next_x, next_y, m, n, word, index + 1)

        # 离开当前节点，回溯，标记回去走过的位置
        board[x][y] = word[index]

        return res

    def exist(self, board: [[str]], word: str) -> bool:
        """
        Time O(n * 3^l)
        Space O(l)
        一模一样的思路，只是用DFS的写法写一遍回溯。区别见注释。
        """
        m = len(board)
        n = len(board[0])

        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    if self.dfs(board, x, y, m, n, word, 0):
                        return True
        return False


class Solution3:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(self, board, x, y, m, n, word, index):
        # 和上一种DFS的区别在这，对于访问是否走到合理的节点，在这里判断而不再进入递归的时候判断，也就是判断当前节点而不是下一个节点
        if board[x][y] != word[index]:
            return False

        # 这里和上一种DFS没区别
        if index == len(word) - 1:
            return True

        board[x][y] = "*"
        res = False
        for direction in self.directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if board[next_x][next_y] == "*":
                continue
            res = res or self.dfs(board, next_x, next_y, m, n, word, index + 1)

        # 离开当前节点，回溯，标记回去走过的位置
        board[x][y] = word[index]

        return res

    def exist(self, board: [[str]], word: str) -> bool:
        """
        Time O(n * 3^l)
        Space O(l)
        一模一样的思路，只是另一种DFS的写法写一遍回溯。区别见注释。
        """
        m = len(board)
        n = len(board[0])

        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    if self.dfs(board, x, y, m, n, word, 0):
                        return True
        return False


s = Solution1()
print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
