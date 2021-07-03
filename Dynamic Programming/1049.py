class Solution:
    def lastStoneWeightII(self, stones: [int]) -> int:
        """
        时间复杂度：O(m * n) , m是石头总重量（准确的说是总重量的一半），n为石头块数
        空间复杂度：O(m)
        本题其实就是尽量让石头分成重量相同的两堆，相撞之后剩下的石头最小，这样就化解成01背包问题了。
        本题物品的重量为store[i]，物品的价值也为store[i]。
        对应着01背包里的物品重量weight[i]和 物品价值value[i]。
        :param stones:
        :return:
        """
        dp = [0] * 15001

        s = sum(stones)

        target = int(s / 2)

        for i in range(len(stones)):    # 遍历物品
            for j in range(target, stones[i] - 1, -1):  # 遍历背包
                # 每一个元素一定是不可重复放入，所以从大到小遍历, 并且容量不能小于当前物品重量，stones[i]
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        # 最后算出来的target是小于等于剩下的数的和的

        return s - dp[target] - dp[target]


s = Solution()
print(s.lastStoneWeightII(stones=[2, 7, 4, 1, 8, 1]))
