from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        Time O(lower - upper)
        Space O(1)
        遍历lower到upper区间，双指针找到不在nums的区间，用一个flag来表示找到区间的开始，此方法超时，因为lower - upper范围过大的时候
        需要遍历的数字比较多。
        """
        res = []
        left = 0
        start = False

        for right in range(lower, upper + 1):
            # 如果找到一个不在nums里面的数字，并且区间开始flag也是false，说明此时找到一个区间的开端，左指针更新并且flag更新
            if right not in nums:
                if start is False:
                    start = True
                    left = right
            # 如果找到一个在nums里面的数字，并且区间开始flag是true，说明找到一个区间的终点，此区间加入结果，并更新flag
            else:
                if start:
                    res.append([left, right - 1])
                    start = False

        # 检查特殊情况，如果nums最大的数字也小于upper的情况
        if start:
            res.append([left, upper])

        return res


class Solution2:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        Time O(n)
        Space O(1)
        三种情况，这次从nums来遍历，速度快很多因为nums一般数字个数远小于lower - upper区间的数字个数。
        """
        n = len(nums)
        res = []
        # 特殊情况，nums里面没有数字
        if n == 0:
            res.append([lower, upper])
            return res

        # 第一种情况：Check for any missing numbers between the lower bound and nums[0].
        if lower < nums[0]:
            res.append([lower, nums[0] - 1])

        # 第二种情况：Check for any missing numbers between successive elements of nums.
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            res.append([nums[i] + 1, nums[i + 1] - 1])

        # 第三种情况：Check for any missing numbers between the last element of nums and the upper bound.
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])

        return res


s = Solution()
print(s.findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99))
