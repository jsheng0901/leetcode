from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        Time O(m * n)
        Space O(m * n)
        初始化前缀和数组，pre_sum[i][j] 记录 matrix 中子矩阵 [0, 0, i-1, j-1] 的元素和
        """
        m, n = len(matrix), len(matrix[0])

        # pre_sum[i][j] 记录 matrix 中子矩阵 [0, 0, i-1, j-1] 的元素和
        self.pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        # 构造前缀和矩阵
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算每个矩阵 [0, 0, i, j] 的元素和
                self.pre_sum[i][j] = self.pre_sum[i - 1][j] + self.pre_sum[i][j - 1] + matrix[i - 1][j - 1] - \
                                     self.pre_sum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Time O(1)
        Space O(1)
        """
        # 目标矩阵之和由四个相邻矩阵运算获得
        result = self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row1][col2 + 1] - self.pre_sum[row2 + 1][col1] + \
                 self.pre_sum[row1][col1]
        return result


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
