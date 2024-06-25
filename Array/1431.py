from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Time O(n)
        Space O(1)
        先找到如果没有额外的糖果最多的糖果是多少，再一次给每个孩子额外的糖果，如果大于等于最大的糖果数，则为true。
        """
        # 找到最多的糖果数量
        greatest_candies = 0
        for candy in candies:
            greatest_candies = max(greatest_candies, candy)

        res = []
        # 一次给每个孩子额外的糖果
        for candy in candies:
            # 如果大于等于最大数，则可行
            if candy + extraCandies >= greatest_candies:
                res.append(True)
            # 反之不行
            else:
                res.append(False)

        return res


s = Solution()
print(s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
print(s.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
