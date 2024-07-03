from typing import List


class Solution1:
    def maxSumAfterPartitioning(self, arr: List[int], k: int):
        """
        Time O(n * k)
        Space O(n)
        bottom-up的DP写法，dp[i]表示到i这个index最大和是多少，那么对应的动态转移公式是
        dp[i] = dp[i - j] + max(subarray[i -1] ... subarray[i -j]) * j
        """

        n = len(arr)
        # 初始化
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # 当前划分点对应的subarray里面最大值是多少
            current_max = 0
            # 最大值取要么是k个数，要么少于k的情况下的个数
            for j in range(1, min(k, i) + 1):
                # 找到subarray里面最大值
                current_max = max(current_max, arr[i - j])
                # 计算最大值，记得适合更新
                dp[i] = max(dp[i], dp[i - j] + current_max * j)

        return dp[n]


class Solution2:
    def dp(self, arr, start_index, k, memo):
        # 走到底，返回0
        if start_index == len(arr):
            return 0

        if memo[start_index] != -1:
            return memo[start_index]

        # 记录当前切割点对应的最大和的值
        tmp = float('-inf')
        # 记录当前切割点对应的subarray里面最大值
        cur_max = float('-inf')
        for i in range(start_index, min(start_index + k, len(arr))):
            # 最大值
            cur_max = max(cur_max, arr[i])
            # 计算第一部分切割的最大值
            first = (i - start_index + 1) * cur_max
            # 后续切割subarray最大值为第二部分
            second = self.dp(arr, i + 1, k, memo)
            # 更新当前切割点对应的最大和
            tmp = max(tmp, first + second)

        # 记录进备忘录
        memo[start_index] = tmp

        return tmp

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        Time O(n * k)
        Space O(n)
        一样的思路只是换成top-down的写法用递归+备忘录来实现。
        """
        # 构建备忘录
        memo = [-1] * len(arr)
        return self.dp(arr, 0, k, memo)


s = Solution2()
print(s.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))
print(s.maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4))
print(s.maxSumAfterPartitioning(arr=[1], k=1))
