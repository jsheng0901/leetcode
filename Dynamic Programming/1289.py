from typing import List


class Solution1:
    def dp(self, grid, i, j, memo, m, n):
        # 返回值保证一定是大于所有path总和的最大值就行，也就是后面去min一定会去掉
        if i < 0 or i >= m or j < 0 or j >= n:
            return 99999

        if i == 0:
            return grid[0][j]

        if memo[i][j] != 6666:
            return memo[i][j]

        # 上一行的所有元素中找到最小值
        sub = float('inf')
        for col in range(n):
            # 但是保证不在同一列
            if col != j:
                sub = min(sub, self.dp(grid, i - 1, col, memo, m, n))

        memo[i][j] = grid[i][j] + sub

        return memo[i][j]

    def minFallingPathSum(self, grid: List[List[int]]) -> float:
        """
        Time O(m * n * n)
        Space O(m * n)
        由于每一行的最小值来源可以是上一行的任意一个数只要不是同一列就行，那么每次递归里面我们需要遍历上一行的所有元素找到最小值。
        其它思路和931一样。
        """
        m, n = len(grid), len(grid[0])
        # 初始值保证不会取到就行，参考题目给的constrict
        memo = [[6666] * n for _ in range(m)]

        res = float('inf')
        for j in range(n):
            res = min(res, self.dp(grid, n - 1, j, memo, m, n))

        return res


class Solution2:
    def minFallingPathSum(self, grid: List[List[int]]) -> float:
        """
        Time O(m * n)
        Space O(m * n)
        Bottom-Up的写法，相比较思路一，我们并不需要在每一行去遍历找最小值，我们完全可以用一个指针存储每一行的最小两个值的index，这样我们每次
        更新直接去找最小值对应的index就行，如果index和当前是同一列，就找第二小的index对应的值，这样每一行的搜索时间变成O(1)。
        """
        # Save the size of the square grid
        n = len(grid)

        # Initialize a two-dimensional array to cache the result of each sub-problem
        memo = [[float('inf')] * n for _ in range(n)]

        # Minimum and Second Minimum Column Index
        next_min1_c = None
        next_min2_c = None

        # Base Case. Fill and save the minimum and second minimum column index
        for col in range(n):
            memo[n - 1][col] = grid[n - 1][col]
            if next_min1_c is None or memo[n - 1][col] <= memo[n - 1][next_min1_c]:
                next_min2_c = next_min1_c
                next_min1_c = col
            elif next_min2_c is None or memo[n - 1][col] <= memo[n - 1][next_min2_c]:
                next_min2_c = col

        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            # Minimum and Second Minimum Column Index of the current row
            min1_c = None
            min2_c = None

            for col in range(n):
                # Select minimum from valid cells of the next row
                if col != next_min1_c:
                    memo[row][col] = grid[row][col] + memo[row + 1][next_min1_c]
                else:
                    memo[row][col] = grid[row][col] + memo[row + 1][next_min2_c]

                # Save minimum and second minimum column index
                if min1_c is None or memo[row][col] <= memo[row][min1_c]:
                    min2_c = min1_c
                    min1_c = col
                elif min2_c is None or memo[row][col] <= memo[row][min2_c]:
                    min2_c = col

            # Change of row. Update next_min1_c and next_min2_c
            next_min1_c = min1_c
            next_min2_c = min2_c

        # Return the minimum from the first row
        return memo[0][next_min1_c]


class Solution3:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(1)
        和思路2一样，只是我们并不需要存储每一行的每个数对应的最小值，完全可以直接用两个指针存储每一行的最小两个值和对应的index，其实第二小的
        对应的index也不需要存储，因为如果当前列和最小的列一样的话，直接赋值和第二小的值即可，不再需要是否是同一列的判断。
        """
        # Save the size of the square grid
        n = len(grid)

        # Minimum and Second Minimum Column Index
        next_min1_c = None
        # 可有可无
        next_min2_c = None

        # Minimum and Second Minimum Value
        next_min1 = None
        next_min2 = None

        # Find the minimum and second minimum from the last row
        for col in range(n):
            if next_min1 is None or grid[n - 1][col] <= next_min1:
                next_min2 = next_min1
                # 可有可无，因为我们不会去判断第二小的列是否是同一列
                next_min2_c = next_min1_c
                next_min1 = grid[n - 1][col]
                next_min1_c = col
            elif next_min2 is None or grid[n - 1][col] <= next_min2:
                next_min2 = grid[n - 1][col]
                # 可有可无
                next_min2_c = col

        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            # Minimum and Second Minimum Column Index of the current row
            min1_c = None
            min2_c = None

            # Minimum and Second Minimum Value of the current row
            min1 = None
            min2 = None

            for col in range(n):
                # Select minimum from valid cells of the next row
                if col != next_min1_c:
                    value = grid[row][col] + next_min1
                # 这里不需要再次判断是否等于第二小的列，因为等于最小的列一定不会等于第二小的列
                else:
                    value = grid[row][col] + next_min2

                # Save minimum and second minimum
                if min1 is None or value <= min1:
                    min2 = min1
                    min2_c = min1_c
                    min1 = value
                    min1_c = col
                elif min2 is None or value <= min2:
                    min2 = value
                    min2_c = col

            # Change of row. Update next_min1_c, next_min2_c, next_min1, next_min2
            next_min1_c = min1_c
            # 可有可无
            next_min2_c = min2_c
            next_min1 = min1
            next_min2 = min2

        # Return the minimum from the first row
        return next_min1


s = Solution3()
print(s.minFallingPathSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
