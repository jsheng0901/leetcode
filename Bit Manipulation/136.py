from typing import List


# 所有位运算的Python基本操作可以参考以下link
# https://realpython.com/python-bitwise-operators/
class Solution1:
    def singleNumber(self, nums: [int]) -> int:
        """
        Time O(n)
        Space O(1)
        异或门^，任何数和自己异或都是0，任何数和0异或都是自己
        """
        single = 0
        for i in range(len(nums)):
            single ^= nums[i]

        return single


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        没出现过的数进入set，出现过的从set移除，最后set只剩下一个数就是single number
        """
        h = set()
        for i in nums:
            if i not in h:
                h.add(i)
            else:
                h.remove(i)

        return h.pop()


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        数学公式计算，对所有数 * 2 - 所有数 = single number
        """
        return 2 * sum(set(nums)) - sum(nums)


s = Solution1()
print(s.singleNumber(nums=[2, 2, 1]))
print(s.singleNumber(nums=[4, 1, 2, 1, 2]))
