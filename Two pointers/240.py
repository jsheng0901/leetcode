from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time O(log(n * m))
        Space O(1)
        因为矩阵是有顺序的，我们从最右上开始，规定指针只能往下或者往左走，如果目标值大于指针，则说明应该往下一层走，
        如果目标值小于指针，说明应该向左走。
        """
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n - 1

        while i < m and j > -1:
            # 找到目标值，此时直接返回
            if matrix[i][j] == target:
                return True
            # 小于目标值，向左走
            elif matrix[i][j] > target:
                j -= 1
            # 大于目标值，向下走
            elif matrix[i][j] < target:
                i += 1

        return False


s = Solution()
print(s.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=5))
