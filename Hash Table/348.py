from collections import defaultdict


class TicTacToe1:

    def __init__(self, n: int):
        self.n = n
        self.row_hash_map = defaultdict(list)
        self.col_hash_map = defaultdict(list)
        self.left_diag_hash_map = defaultdict(int)
        self.right_diag_hash_map = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Time O(n)
        Space O(n)
        用四个hash map存储所有四个方向的数字，每次遍历所有四个方向判断是否是一模一样的元素。
        """
        # 添加新的到对应的行和列
        self.row_hash_map[row].append(player)
        self.col_hash_map[col].append(player)

        # 对角线
        if row == col:
            self.left_diag_hash_map[(row, col)] = player

        # 对角线
        if row + col == self.n - 1:
            self.right_diag_hash_map[(row, col)] = player

        # 如果行或者列都是1
        if len(self.row_hash_map[row]) == self.n and all([i == 1 for i in self.row_hash_map[row]]) or (
                len(self.col_hash_map[col]) == self.n and all([i == 1 for i in self.col_hash_map[col]])):
            return 1

        # 如果行或者列都是2
        if len(self.row_hash_map[row]) == self.n and all([i == 2 for i in self.row_hash_map[row]]) or (
                len(self.col_hash_map[col]) == self.n and all([i == 2 for i in self.col_hash_map[col]])):
            return 2

        # 如果对角线都是1
        if len(self.left_diag_hash_map) == self.n and all([i == 1 for i in self.left_diag_hash_map.values()]) or (
                len(self.right_diag_hash_map) == self.n and all([i == 1 for i in self.right_diag_hash_map.values()])):
            return 1

        # 如果对角线都是2
        if len(self.left_diag_hash_map) == self.n and all([i == 2 for i in self.left_diag_hash_map.values()]) or (
                len(self.right_diag_hash_map) == self.n and all([i == 2 for i in self.right_diag_hash_map.values()])):
            return 2

        return 0


class TicTacToe2:

    def __init__(self, n: int):
        self.n = n
        self.horiz = [0] * n
        self.vert = [0] * n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Time O(1)
        Space O(n)
        其实可以利用正负属性，如果用户1，计数为1，用户2，计数为 -1，这样只有四个方向的和的绝对值都是n的情况的时候才表示当前用户赢
        """
        # 标记计数参数
        move = 1
        if player == 2:
            move = -1

        # 更新四个方向
        self.horiz[col] += move
        self.vert[row] += move

        # 对角线
        if row == col:
            self.diag1 += move
        if row + col == self.n - 1:
            self.diag2 += move

        # 四个方向如果有一个满足，说明当前的用户赢了
        if (abs(self.horiz[col]) == self.n or abs(self.vert[row]) == self.n or abs(self.diag1) == self.n
                or abs(self.diag2) == self.n):

            return player

        return 0


obj = TicTacToe2(n=2)
print(obj.move(0, 1, 1))
print(obj.move(1, 1, 2))
print(obj.move(1, 0, 1))
