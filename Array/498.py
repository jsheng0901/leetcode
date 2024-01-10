from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Time O(m * n)
        Space O(min(m, n))
        先把所有对角线的遍历拿出来，然后遇到偶数的对角线我们在reverse一下顺序放进最后的结果。
        """
        # check是否有matrix
        if not mat or not mat[0]:
            return []

        res = []
        m = len(mat)
        n = len(mat[0])

        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        # 所有对角线的起点在第一行或者最后一列
        for d in range(m + n - 1):
            # Clear the intermediate array everytime we start
            # to process another diagonal
            # 每一次初始化每次对角线的临时数组
            tmp = []

            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            # 每一条对角线的第一个数字位置
            row = 0 if d < n else d - n + 1
            col = d if d < n else n - 1

            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            # 遍历对角线从右往左下方向
            while row < m and col > -1:
                tmp.append(mat[row][col])
                row += 1
                col -= 1

            # Reverse even numbered diagonals.
            # because here, the index number
            # is starting from 0
            # 翻转index是偶数的对角线
            if d % 2 == 0:
                res.extend(tmp[::-1])
            else:
                res.extend(tmp)

        return res


s = Solution()
print(s.findDiagonalOrder(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
