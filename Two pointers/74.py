class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        """
        核心思想还是二分法查找，二维数组转化成一维数组，难点在于mid在一维数组的index转化成二维数组的index
        row: mid // col
        column: mid % col
        :param matrix:
        :param target:
        :return:
        """
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        m = len(matrix)
        n = len(matrix[0])

        while left <= right:
            mid = left + (right - left) // 2
            new_mid_row = mid // n
            new_mid_column = mid % n

            if matrix[new_mid_row][new_mid_column] == target:
                return True

            if matrix[new_mid_row][new_mid_column] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False