from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        倒序遍历，保证每一个数都是升序，遇到比前一个数大的数的时候，我们需要split当前数，最好的办法是split后保证最小的数也是最大的情况，
        这样后续如果还有要split也不需要split太多数，详细见注释。
        """
        answer = 0
        n = len(nums)

        # Start from the second last element, as the last one is always sorted.
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if nums[i] <= nums[i + 1]:
                continue

            # Count how many elements are made from breaking nums[i].
            # 这里如果是整除的情况， nums[i] // nums[i + 1]
            # 如果不是整除的情况，（nums[i] // nums[i + 1]） + 1
            # 合在一起变成一个公式，核心思想在这里
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

            # It requires numElements - 1 replacement operations.
            answer += num_elements - 1

            # Maximize nums[i] after replacement.
            # 最大化分完后的数，保证后续split操作最少
            nums[i] = nums[i] // num_elements

        return answer


s = Solution()
print(s.minimumReplacement(nums=[12, 9, 7, 6, 17, 19, 21]))
