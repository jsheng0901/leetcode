from collections import defaultdict
from typing import List


class Solution1:
    def reverse_number(self, num):
        # reverse number的标准写法
        reversed_num = 0
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10

        return reversed_num

    def countNicePairs(self, nums: List[int]) -> int:
        """
        Time O(n^2)
        Space O(1)
        暴力搜索所有组合index，每一对都判断一下是否符合题目的equation要求。
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # 得到function左右的数字
                left = nums[i] + self.reverse_number(nums[j])
                right = nums[j] + self.reverse_number(nums[i])
                # 判断是否相等，相等则答案 +1
                if left == right:
                    res += 1

        return res


class Solution2:
    def reverse_number(self, num):

        reversed_num = 0
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10

        return reversed_num

    def countNicePairs(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        其实这个背后是个数学题，对于nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) 可以转化成
        nums[i] - rev(nums[i])) == (nums[j] - rev(nums[j])，所以我们可以计算出每个数和自己reverse的差值，然后直接找到差值一样的所有
        组合个数。用一个hashmap来记录所有出现的频率，然后查找出现个数。详细见注释
        """
        # 记录差值的数组
        reverse_nums_diff = []
        for num in nums:
            reversed_num = self.reverse_number(num)
            reverse_nums_diff.append(num - reversed_num)

        res = 0
        mod = 10 ** 9 + 7
        freq = defaultdict(int)
        for diff in reverse_nums_diff:
            # 如果没有出现过，+0，如果出现过，可以组成的index对数就是之前出现的频率。
            res += (freq[diff] % mod)
            freq[diff] += 1
            # 另一种写法来记录出现个数，更直观表示逻辑
            # if diff in freq:
            #     res += freq[diff]
            #     freq[diff] += 1
            # else:
            #     freq[diff] = 1

        return res % mod


s = Solution2()
print(s.countNicePairs(nums=[42, 11, 1, 97]))
