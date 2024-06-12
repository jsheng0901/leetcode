from typing import List


class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        用一个set来记录出现过的数，如果出现过说明是duplicate的数字，记录进结果。有一个额外空间使用，其实不符合题目要求，但是可以过所有TC。
        """
        seen = set()
        res = []

        for num in nums:
            # 如果出现过，说明是duplicate，记录进结果
            if num not in seen:
                seen.add(num)
            # 如果没有出现过，记录进set
            else:
                res.append(num)

        return res


class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(1)
        因为题目里面的数字刚好是[1, n]的区间，也就是说，同一个数字对应的index应该是一样的，如果出现过一次，我们把它变成负数，如果是负数，
        说明之前出现过，记录进结果。这里要用绝对值，因为如果是negative数字，则index毫无意义，不过题目已经说明了数字所在的区间，所以也没问题。
        """
        res = []
        for num in nums:
            # 注意索引，元素大小从 1 开始，有一位索引偏移
            if nums[abs(num) - 1] < 0:
                # 之前已经把对应索引的元素变成负数了，
                # 这说明 num 重复出现了两次
                res.append(abs(num))
            else:
                # 把索引 num - 1 置为负数
                nums[abs(num) - 1] *= -1

        return res


s = Solution2()
print(s.findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDuplicates(nums=[1, 1, 2]))
print(s.findDuplicates(nums=[1]))
