from itertools import accumulate
from typing import List


class Solution1:
    def totalStrength(self, strength: List[int]) -> int:
        """
        Time O(n^2)
        Space O(1)
        遍历所有subarray的组合，同时查重这个subarray的最小值和记录总和，来计算total strength。
        """
        total_strength = 0

        for i in range(len(strength)):
            # 当前只有一个数的时候，最小值和总和都是自己
            min_strength = strength[i]
            sum_strength = strength[i]
            total_strength += min_strength * sum_strength
            for j in range(i + 1, len(strength)):
                # 更新subarray的最小值
                min_strength = min(min_strength, strength[j])
                # 更新subarray的总和
                sum_strength += strength[j]
                total_strength += min_strength * sum_strength

        return total_strength % (10 ** 9 + 7)


class Solution2:
    def totalStrength(self, strength: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        此题有很多数学思路，核心思想，用前缀和快速计算一定区间的总和，用单调栈来记录当这个数作为最小值在subarray的时候的左右终点index。
        详细见注释和leetcode的tutorial https://leetcode.com/problems/sum-of-total-strength-of-wizards/editorial/
        """
        mod = 10 ** 9 + 7
        n = len(strength)

        # Get the first index of the non-larger value to strength[i]'s right.
        right_index = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                right_index[stack.pop()] = i
            stack.append(i)

        # Get the first index of the smaller value to strength[i]'s left.
        left_index = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                left_index[stack.pop()] = i
            stack.append(i)

        # prefix sum of the prefix sum array of strength.
        presum_of_presum = list(accumulate(accumulate(strength, initial=0), initial=0))

        answer = 0
        for i in range(n):
            # Get the left index and the right index.
            left_bound = left_index[i]
            right_bound = right_index[i]

            # Get the left_count and right_count (marked as L and R in the previous slides)
            left_count = i - left_bound
            right_count = right_bound - i

            # Get positive presum and the negative presum.
            neg_presum = (presum_of_presum[i + 1] - presum_of_presum[i - left_count + 1]) % mod
            pos_presum = (presum_of_presum[i + right_count + 1] - presum_of_presum[i + 1]) % mod

            # The total strength of all subarrays that have strength[i] as the minimum.
            answer += strength[i] * (pos_presum * left_count - neg_presum * right_count)
            answer %= mod

        return answer


s = Solution1()
print(s.totalStrength(strength=[1, 3, 1, 2]))
