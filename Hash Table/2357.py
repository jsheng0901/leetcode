from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        统计有多少个unique的非0数及我们要最少的操作次数
        """
        # 记录所有非0的unique数
        num_set = set()
        for n in nums:
            if n != 0:
                num_set.add(n)

        # 统计长度及次数
        return len(num_set)


s = Solution()
print(s.minimumOperations(nums=[1, 5, 0, 3, 5]))
