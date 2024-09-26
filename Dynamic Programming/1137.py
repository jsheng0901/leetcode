class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Time O(n)
        Space O(1)
        很简单的动态规划题，三个参数存储每一步需要的状态。
        """
        # 初始化三个参数，存储状态
        n0 = 0
        n1 = 1
        n2 = 1
        # 特殊情况，直接返回
        if n == 0:
            return n0

        # 遍历剩下的所有数
        for i in range(3, n + 1):
            # 新的结果
            tmp = n0 + n1 + n2
            # 状态转移
            n0 = n1
            n1 = n2
            n2 = tmp

        return n2


s = Solution()
print(s.tribonacci(n=4))
print(s.tribonacci(n=25))
