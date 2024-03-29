class Solution1:
    def isToeplitzMatrix(self, matrix: [[int]]) -> bool:
        """
        Time O(n * m)
        Space O(1)
        check 斜对角的list是否相等
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows - 1):
            if matrix[i][:cols - 1] != matrix[i + 1][1:]:  # list compare will do O(m)
                return False
        return True


class Solution2:
    def isToeplitzMatrix(self, matrix: [[int]]) -> bool:
        """
        Time O(n * m)
        Space O(1)
        check斜对角是否相等，but kind of slow on LeetCode then above without build-in list compare
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


s = Solution2()
print(s.isToeplitzMatrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
