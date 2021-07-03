class Solution:
    def canPartition(self, nums: [int]) -> bool:
        """
        time O(n), space O(n)
        01 背包问题的应用,
        物品是nums[i]，重量是nums[i]，价值也是nums[i]，背包体积是sum/2
        :param nums:
        :return:
        """
        # dp[i] 中的i表示背包内总和
        # 题目中说：每个数组中的元素不会超过100，数组的大小不会超过200
        # 那么背包内总和不会大于20000，及target不会超过20000, 所以定义一个20001（包括0）大的数组。

        dp = [0] * 20001

        s = sum(nums)

        if s % 2 == 1:
            return False

        target = int(s / 2)

        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                # 每一个元素一定是不可重复放入，所以从大到小遍历, 并且容量不能小于当前物品重量，及nums[i]
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        # 集合中的元素正好可以凑成总和target
        if dp[target] == target:
            return True

        return False
