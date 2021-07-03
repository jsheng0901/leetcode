class Solution:
    def maxProfit(self, prices: [int], fee: int) -> int:
        """
        time O(n), space O(1), 此题更适合动态规划的思路，贪心的思路只是锻炼
        情况一：收获利润的这一天并不是收获利润区间里的最后一天（不是真正的卖出，相当于持有股票），所以后面要继续收获利润。
        情况二：前一天是收获利润区间里的最后一天（相当于真正的卖出了），今天要重新记录最小价格了。
        情况三：不作操作，保持原有状态（买入，卖出，不买不卖）
        :param prices:
        :param fee:
        :return:
        """

        result = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            # 情况二：相当于买入
            if prices[i] < min_price:
                min_price = prices[i]

            # 情况三：保持原有状态（因为此时买则不便宜，卖则亏本）
            if min_price <= prices[i] <= min_price + fee:
                continue

            # 计算利润，可能有多次计算利润，最后一次计算利润才是真正意义的卖出
            if prices[i] > min_price + fee:
                result += prices[i] - min_price - fee
                min_price = prices[i] - fee  # 此处减fee很重要，等同于和之前抵消
                # 因为如果还在收获利润的区间里，表示并不是真正的卖出，而计算利润每次都要减去手续费，
                # 所以要让minPrice = prices[i] - fee;，这样在明天收获利润的时候，才不会多减一次手续费！

        return result


s = Solution()
print(s.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
