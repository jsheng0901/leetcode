class Solution:
    def get_cur_sum(self, n, index, val):
        count = 0

        # On index's left:
        # If value > index, there are index + 1 numbers in the arithmetic sequence:
        # [value - index, ..., value - 1, value].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [1, 2, ..., value - 1, value], plus a sequence of length (index - value + 1) of 1s.
        if val > index:
            count += ((val + val - index) * (index + 1)) // 2
        else:
            count += ((val + 1) * val) // 2 + (index - val + 1)

        # On index's right:
        # If value >= n - index, there are n - index numbers in the arithmetic sequence:
        # [value, value - 1, ..., value - n + 1 + index].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [value, value - 1, ..., 1], plus a sequence of length (n - index - value) of 1s.
        if val >= n - index:
            count += ((val + val - n + 1 + index) * (n - index)) // 2
        else:
            count += ((val + 1) * val) // 2 + (n - index - val)

        # 重复计算了两次，需要减一次
        return count - val

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Time O(log(maxSum))
        Space O(1)
        在区间内猜最大值，然后根据最大值，找到组合成数组后最小的总和的情况，之后就是找左边界的的标准二分法写法，找到第一个小于左边界的值。
        此题难点在于如果构建数组，并且找到组成数组后的最小值。
        """
        left = 1
        right = maxSum

        while left <= right:
            mid = left + (right - left) // 2
            # 得到当前情况小的最小值组合
            cur_sum = self.get_cur_sum(n, index, mid)

            if cur_sum < maxSum:
                left = mid + 1
            elif cur_sum > maxSum:
                right = mid - 1
            elif cur_sum == maxSum:
                left = mid + 1

        return right


s = Solution()
print(s.maxValue(n=8, index=7, maxSum=14))
print(s.maxValue(n=4, index=0, maxSum=4))
