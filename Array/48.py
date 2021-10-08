class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        # transpose matrix, 对角线置换先，再reverse每一行，及达到旋转90度
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # reverse each row
        for i in range(n):
            matrix[i].reverse()

