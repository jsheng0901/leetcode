class Solution:
    def maxProfit(self, inventory: [int], orders: int) -> int:
        """
        O(nlog(n)) time, O(1) space
        binary search to find threshold of 所有球寻找一个介于0和最大inventory的数字mid，使得全部球中，
        大于mid的球数都被卖掉，一部分（也可以是0）等于mid的球数被卖掉, 之后剩下的球找到阈值后，用数学公式计算当前数字和阈值数字
        中间的差，此数字就是卖出去的总和
        """
        inventory.sort()
        left = 0
        right = inventory[-1]

        while left < right:
            mid = left + (right - left) // 2

            count = 0
            for i in inventory:
                if i > mid:
                    count += i - mid

            if count > orders:
                left = mid + 1
            else:
                right = mid

        mid = left + (right - left) // 2
        ans = 0
        for i in inventory:
            if i > mid:
                ans += i * (i + 1) // 2 - mid * (mid + 1) // 2      # 计算数值总和，数学公式
                orders -= i - mid       # 计算还有多少order

        ans += orders * mid     # 如果剩下还有没有卖完的，就用阈值去卖
        return int(ans) % (10 ** 9 + 7)


s = Solution()
print(s.maxProfit(inventory=[2, 8, 4, 10, 6], orders=20))
