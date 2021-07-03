class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        """
        设置上下左右线，loop完哪一行数据就对应的增加或减少哪一条线
        :param matrix:
        :return:
        """
        top_line = 0
        bottom_line = len(matrix)
        left_line = 0
        right_line = len(matrix[0])
        result = []

        while bottom_line > top_line and right_line > left_line:

            top = matrix[top_line][left_line: right_line]
            result.extend(top)
            top_line += 1
            if top_line >= bottom_line:
                break

            right = [m[right_line - 1] for m in matrix[top_line: bottom_line]]
            result.extend(right)
            right_line -= 1
            if left_line >= right_line:
                break

            bottom = matrix[bottom_line - 1][left_line: right_line]
            result.extend(bottom[::-1])
            bottom_line -= 1
            if top_line >= bottom_line:
                break

            left = [m[left_line] for m in matrix[top_line: bottom_line]]
            result.extend(left[::-1])
            left_line += 1

        return result

