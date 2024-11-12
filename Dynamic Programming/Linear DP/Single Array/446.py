from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        参考1027的思路，我们需要找到的是nums[i] - nums[j]的差值在nums[j]结尾的情况下出现过多少次。同时记录当前i结尾的时候差值的出现次数
        状态。详细见注释。
        """
        # 存储所有状态，用字典，因为这里我们不知道差值可能的所有情况
        dp = {}
        res = 0
        # 遍历所有组合i > j的情况下
        for i in range(1, len(nums)):
            for j in range(i):
                # 差值
                diff = nums[i] - nums[j]
                # 当前数的差值状态，等于前一个j同样状态下的次数 + 1，并且累计自己
                dp[(i, diff)] = dp.get((i, diff), 0) + dp.get((j, diff), 0) + 1
                # 注意计算结果的时候，累加的是j这个状态，因为在(i, diff)同样的状态下(j, diff)一定是刚好可以和i组成等差数列的次数。
                # 不能累加i的状态，因为i记录的是出现差值状态的次数，可能两个数也会被记录，但是不能构成等差数列。详细见例子1。
                res += dp.get((j, diff), 0)

        return res


s = Solution()
print(s.numberOfArithmeticSlices(nums=[2, 2, 3, 4]))
print(s.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
print(s.numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
