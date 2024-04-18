from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        数学题，贪心思想，因为要最小次数，所以每次能用3就用3，直到不能用3就用2。四种情况对应操作，详细见注释。
        """
        freq = Counter(nums)
        res = 0
        for v in freq.values():
            # 等于1，说明不可能被消除，直接返回 -1
            if v == 1:
                return -1
            # 被3整除，全都用3
            elif v % 3 == 0:
                res += v // 3
            # 被3整除余1，需要两次2先，再用3，比如 13 -> 9 + 4
            elif v % 3 == 1:
                res += (v // 3) - 1 + 2
            # 被3整除余2，需要一次2先，再用3，比如 5 -> 3 + 2
            elif v % 3 == 2:
                res += v // 3 + 1

        return res


s = Solution()
print(s.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(s.minOperations(nums=[2, 1, 2, 2, 3, 3]))
