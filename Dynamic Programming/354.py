from typing import List


class Solution1:
    def lis(self, nums):
        # 动态规划找最长递增子序列，同300
        dp = [1] * len(nums)
        result = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    result = max(result, dp[i])

        return result

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Time O(nlog(n) + n^2)   sort + LIS
        Space O(n)
        这题神奇的地方在于先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序；
        之后把所有的 h 作为一个数组，在这个数组上计算 LIS 的长度就是答案。
        因为首先，对宽度 w 从小到大排序，确保了 w 这个维度可以互相嵌套，所以我们只需要专注高度 h 这个维度能够互相嵌套即可。
        其次，两个 w 相同的信封不能相互包含，所以对于宽度 w 相同的信封，对高度 h 进行降序排序，
        保证二维 LIS 中不存在多个 w 相同的信封（因为题目说了长宽相同也无法嵌套）。
        之后就是嵌套LIS算法找到最长递增子序列。但是传统LIS的算法需要n^2的时间复杂度，并不能通过所有测试数据。
        """
        # 按宽度升序排列，如果宽度一样，则按高度降序排列
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        height = [0] * len(envelopes)

        # 初始化height，其实就是每个信封的高度
        for i in range(len(envelopes)):
            height[i] = envelopes[i][1]

        # 对高度数组寻找 LIS
        return self.lis(height)


class Solution2:
    def lis(self, nums):
        # 牌顶数组初始化为 0，这里初始化长度为数组长度，因为最长情况下整个数组都是递增的
        n = len(nums)
        top = [0] * n
        # 牌堆数初始化为 0
        piles = 0

        for i in range(len(nums)):
            # 要处理的扑克牌
            poker = nums[i]

            # 搜索左侧边界的二分查找，这里为什么左边界可以是因为左边界出循序的结果是left = right + 1，
            # 如果找不到的时候及poker大于牌堆上面的所有数的时候，left出循环的时候刚好等于需要新牌堆的个数，
            # 同时如果找的到的时候，左边界是我们刚好需要的结果，保证牌堆顶从左到右有序。
            left, right = 0, piles - 1
            while left <= right:
                mid = left + (right - left) // 2
                if top[mid] > poker:
                    right = mid - 1
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid - 1

            # 如果没有合适的牌堆，此时刚好left出循序
            if left == piles:
                piles += 1

            # 把这张牌放到牌堆顶，持续更新牌堆顶的最小数值
            top[left] = poker

        # 牌堆数就是 LIS 长度
        return piles

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Time O(nlog(n))     sort + 二分法查找 = nlog(n) + nlog(n) = nlog(n)
        Space O(n)
        整体逻辑一模一样和第一种解法。区别在于用二分法来查找LIS。
        二分法查找类似一种纸牌游戏，
        参考link：https://labuladong.github.io/algo/di-er-zhan-a01c6/zi-xu-lie--6bc09/dong-tai-g-6ea57/
        """
        # 同上
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        height = [0] * len(envelopes)
        for i in range(len(envelopes)):
            height[i] = envelopes[i][1]

        return self.lis(height)


s = Solution2()
print(s.maxEnvelopes(envelopes=[[5, 4], [6, 4], [6, 7], [2, 3]]))
