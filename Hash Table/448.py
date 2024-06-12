from typing import List


class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        构建字典存储出现过的数字，方便后续快速check是否存在，之后遍历 1 - n 所有数字，如果出现过在字典里面就跳过，没有出现过说明不存在之前的
        数组内，加入结果。
        """
        # 用set来存储出现过的数字，达到O(1)的速度查存在
        hash_map = set()
        for num in nums:
            hash_map.add(num)

        res = []
        # 遍历所有应该存在的数字 1 - n
        for num in range(1, len(nums) + 1):
            # 如果没有出现过加入结果
            if num not in hash_map:
                res.append(num)

        return res


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        同思路1，只是这里用数组来记录出现过的数字。
        """
        count = [0] * len(nums)

        # 注意这里的 index，比如数字4，对应的 index 应该是3
        for num in nums:
            count[num - 1] = num

        res = []
        # 遍历应该存在的数组
        for i, val in enumerate(count):
            # 如果结果为0，说明没有出现过这里对应的index，注意具体数值应该是 index + 1
            if val == 0:
                res.append(i + 1)

        return res


class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(1)
        同思路2，只是这里把记录是否出现过的数组和原始数组合二为一。同442思路。用变成负数来标记是否出现过。
        """
        for num in nums:
            # 注意索引，元素大小从 1 开始，有一位索引偏移
            if nums[abs(num) - 1] < 0:
                # 之前已经把对应索引的元素变成负数了，注意这里是用绝对值，不然负数没有意义
                # 这说明 num 重复出现了
                # 直接跳过
                continue
            else:
                # 把索引 num - 1 置为负数
                nums[abs(num) - 1] *= -1

        # 遍历没有被标记过的数，同理数值应该是 index + 1
        res = []
        for i, val in enumerate(nums):
            if val > 0:
                res.append(i + 1)

        return res


s = Solution3()
print(s.findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDisappearedNumbers(nums=[1, 1]))
