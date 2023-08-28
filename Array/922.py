from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        loop一次，记录奇数偶数下标，如果是偶数放进偶数index，如果是奇数放进奇数index。
        """
        result = [0] * len(nums)
        even_index = 0
        odd_index = 1
        for i in range(len(nums)):
            # 偶数
            if nums[i] % 2 == 0:
                result[even_index] = nums[i]
                even_index += 2
            else:
                result[odd_index] = nums[i]
                odd_index += 2

        return result


s = Solution()
print(s.sortArrayByParityII(nums=[4, 2, 5, 7]))
