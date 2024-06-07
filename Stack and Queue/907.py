from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        单调栈思路，找到所有subarray里面所有最小值是O(n^2)的操作，可以反过来找每个数字是最小值的时候出现的subarray的频率。
        问题转化成，每个数字找左边比他小的第一个数和右边比他小的第一个数，这样在左右边界内当前数字最小，计算此时边界内的subarray的个数。
        如何找左右边界，此题转换找下一个比当前数字更小的数，单调递增栈刚好满足此条件。
        详细见注释。参考 https://leetcode.com/problems/sum-of-subarray-minimums/editorial/
        """
        mod = 10 ** 9 + 7
        stack = []
        res = 0
        # 遍历所有数字，注意这里因为需要计算最后一个数字构成的subarray的频率，需要再向前走一步
        for i in range(len(arr) + 1):
            # 当栈存在并且当前数字小于等于栈顶数字或者栈内只有最后一个数字的时候，等于的情况是对应[2, 2, 2]
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                # 弹出栈顶，也就是我们要找的当前最小值的index
                mid = stack.pop()
                # 左边界如果栈内还有元素，那此时栈顶的一定是第一个左边更小的数，如果是空栈，则index为-1，为了计算左边的个数
                left_boundary = -1 if not stack else stack[-1]
                # 右边界就是当前更小的这个数的index
                right_boundary = i
                # 这里有个计算两个边界内subarray的公式，分布是左边界到中心点的距离 * 右边界到中心点的距离
                count = (mid - left_boundary) * (right_boundary - mid)
                # 出现频率 * 数字本身，然后叠加
                res += count * arr[mid]

            # 如果大于当前栈顶，或者空栈，直接入栈保证栈内是从底到上单调递增
            stack.append(i)

        return res % mod


s = Solution()
print(s.sumSubarrayMins(arr=[3, 1, 2, 4]))
print(s.sumSubarrayMins(arr=[11, 81, 94, 43, 3]))
print(s.sumSubarrayMins(arr=[2, 2, 2]))
