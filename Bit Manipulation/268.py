from typing import List


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        数学思路，等差数列求和找到期待值，具体数组求和找到实际值，相减找到缺失值。
        """
        n = len(nums)
        # 等差数列求和公式：(首项 + 末项) * 项数 / 2
        expect = (0 + n) * (n + 1) / 2
        actual = 0
        for x in nums:
            actual += x

        return int(expect - actual)


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        构建set，每次查询是否在set里面，查询的时候可以降低到O(1)的时间。
        """
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        位运算的XOR的核心思想：一个数和它本身做异或运算结果为 0，一个数和 0 做异或运算还是它本身。并且XOR满足交换律。
        所以没有缺失的数和自己的index做XOR一定成对出现并且结果为0，最后那个落单的index就是自己缺失的那个数。
        比如 missing = 4 ^ (0 ^ 0) ^ (1 ^ 1) ^ (2 ^ 3) ^ (3 ^ 4)
                    = (4 ^ 4) ^ (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ 2
                    = 0 ^ 0 ^ 0 ^ 0 ^ 2
                    = 2
        """
        n = len(nums)
        res = 0
        # 先和新补的索引异或一下
        res ^= n
        # 和其他的元素、索引做异或
        for i in range(n):
            res ^= i ^ nums[i]
        return res


s = Solution3()
print(s.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber(nums=[3, 0, 1]))
