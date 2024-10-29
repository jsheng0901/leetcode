from typing import List


class Solution1:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        """
        Time: O(n * m)      n为正数个数，m为背包容量
        Space: O(m)         m为背包容量

        假设加法的总和为x，那么减法对应的总和就是sum - x。
        所以我们要求的是 x - (sum - x) = S
        x = (S + sum) / 2
        此时问题就转化为，装满容量为x背包，有几种方法。
        """
        s = sum(nums)
        if target > s:
            return 0

        if (s + target) % 2 == 1:
            return 0

        big_size = int((s + target) / 2)
        dp = [0] * (big_size + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(big_size, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[-1]


class Solution2:
    def dp(self, nums, index, total, target, memo):
        # 走到底了
        if index == len(nums):
            # 如果相等，返回找到一条合理的path 1
            if total == target:
                return 1
            # 不相等，说明此path不通，返回 0
            return 0

        # 注意这里备忘录用的是字典，需要把它俩转成字符串才能作为字典的key
        key = str(index) + "," + str(total)
        # 避免重复计算
        if key in memo:
            return memo[key]

        # 子节点所有返回值叠加
        sub = 0
        # 穷举两种情况
        sub += self.dp(nums, index + 1, total + nums[index], target, memo)
        sub += self.dp(nums, index + 1, total - nums[index], target, memo)

        # 记入备忘录
        memo[key] = sub

        return sub

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Time O(t * n)  n --> length of nums  t --> sum of nums array
        Space O(t * n)
        此方法是回溯的基础上进行减枝，其实就DP的思路，带备忘录的DFS就是DP。每个数字有两种选择，加号或者减号，遍历所有情况找到符合条件的path，
        用备忘录进行减枝即可。
        """
        # 构建备忘录，这里和一些题目不一样的地方在于备忘录没有用数组，用字典可以不限制初始化备忘录大小
        # 第二个状态total和最多是sum of nums array，所以也可以初始化数组备忘录为
        # memo = [[-1] * len(nums) for _ in range(2 * sum + 1)]
        # 这里为什么是 2 * sum + 1，因为我们需要index是正数，所以in case全都是负号的情况下，还是能保证备忘录的index是正数
        # 相对应的我们存储进memo时候应该是 memo[i][sum + total] 第二个index为当前总和 + nums的总和。
        memo = {}
        return self.dp(nums, 0, 0, target, memo)


s = Solution1()
print(s.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
