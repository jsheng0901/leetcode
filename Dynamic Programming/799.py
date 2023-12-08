class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Time O(row * col --> 1)
        Space O(row * col --> 1)
        动态规划思路，dp[i][j] 表示到当前香槟我们有多少流进来的香槟，流出去的香槟只会流到下面 [i+1][j] 和 [i+1][j+1] 这两层。
        """
        # 构建动态规划数组，这里直接构建100层因为题目有说上线100层
        dp = []
        for row in range(100 + 1):
            dp.append([0] * (row + 1))
        # 初始化第一层是原始值，因为我们最开始倒入所有的香槟
        dp[0][0] = poured

        # 遍历到我们想要search的层
        for i in range(query_row):
            # 遍历所有列
            row = dp[i]
            for j in range(len(row)):
                # 当前拥有的香槟算出有多少多余的
                remain = (dp[i][j] - 1) / 2
                # 如果有多余的则会流到下一层
                if remain > 0:
                    dp[i + 1][j] += remain
                    dp[i + 1][j + 1] += remain

        # 取最小值，大于1说明我们装满了
        return min(1, dp[query_row][query_glass])


s = Solution()
print(s.champagneTower(poured=1, query_row=1, query_glass=1))
print(s.champagneTower(poured=2, query_row=1, query_glass=1))
print(s.champagneTower(poured=100000009, query_row=33, query_glass=17))
