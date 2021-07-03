class Solution:
    def candy(self, ratings: [int]) -> int:
        """
        time O(n), space O(n)
        这道题目一定是要确定一边之后，再确定另一边，例如比较每一个孩子的左边，然后再比较右边，「如果两边一起考虑一定会顾此失彼」
        此时局部最优：只要右边评分比左边大，右边的孩子就多一个糖果，全局最优：相邻的孩子中，评分高的右孩子获得比左边孩子更多的糖果
        那么本题我采用了两次贪心的策略：
            一次是从左到右遍历，只比较右边孩子评分比左边大的情况。
            一次是从右到左遍历，只比较左边孩子评分比右边大的情况。
        一定要两次顺序相反的比遍历，不然就没办法利用之前遍历的结果来进行判断
        :param ratings:
        :return:
        """
        candy = [1] * len(ratings)

        # 从前向后
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        # 从后向前
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candy[j] = max(candy[j], candy[j + 1] + 1)

        result = 0
        for c in candy:
            result += c

        return result


s = Solution()
print(s.candy(ratings=[1, 0, 2]))
