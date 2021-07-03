class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        """
        完全背包问题，用动态规划更快
        本质是本题求的是排列总和，而且仅仅是求排列总和的个数，并不是把所有的排列都列出来。
        如果本题要把排列都列出来的话，只能使用回溯算法爆搜。

        如果求组合数就是外层for循环遍历物品，内层for遍历背包。
        如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        :param nums:
        :param target:
        :return:
        """
        dp = [0] * (target + 1)

        dp[0] = 1

        for i in range(target + 1):
            for j in range(0, len(nums)):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]


s = Solution()
print(s.combinationSum4(nums=[1, 2, 3], target=4))
