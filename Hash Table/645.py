from typing import List


class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        先记录数字进set，如果出现过就是duplicate的那个数字，之后再遍历 1 - n，如果不在set里面，说明是missing的那个数字。
        """
        res = []
        hash_map = set()
        # 记录出现过的数字
        for num in nums:
            if num in hash_map:
                # 找到 duplicate 的那个数字
                res.append(num)
            else:
                hash_map.add(num)

        for i in range(1, len(nums) + 1):
            # 找到 missing 的那个数字
            if i not in hash_map:
                res.append(i)

        return res


class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(1)
        同442，448的思路，用数组本身作为hash_map。详细见注释。
        """
        res = []
        for num in nums:
            # 注意索引，元素大小从 1 开始，有一位索引偏移
            if nums[abs(num) - 1] < 0:
                # 之前已经把对应索引的元素变成负数了，
                # 这说明 num 重复出现了两次
                # 找到 duplicate 的那个数字
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1

        # 遍历没有被标记过的数，同理数值应该是 index + 1
        for i, val in enumerate(nums):
            if val > 0:
                res.append(i + 1)

        return res


s = Solution2()
print(s.findErrorNums(nums=[1, 2, 2, 4]))
print(s.findErrorNums(nums=[1, 1]))
