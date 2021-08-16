class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        return

    def dimensions(self) -> list:
        return


class Solution1:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """对每一行进行binary search， 因为是有序的每一行的数字"""
        dim = binaryMatrix.dimensions()
        rows = dim[0]
        cols = dim[1]
        smallest_index = cols
        for r in range(rows):
            left = 0
            right = smallest_index - 1      # 这里我们可以优化最远的起始点，因为我们只需要找比上一个更新的index的column
            while left < right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(r, mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            if binaryMatrix.get(r, left) == 1:
                smallest_index = min(smallest_index, left)

        return -1 if smallest_index == cols else smallest_index


class Solution2:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1

        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:     # 如果是1往左边走，如果是0往下面走
                current_row += 1
            else:
                current_col -= 1

        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1
