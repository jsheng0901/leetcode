from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        """
        Time O(n)
        Space O(1)
        遇到1就累加，遇到0就初始化tmp
        """
        result = 0
        tmp = 0
        for i in range(len(nums)):
            # 如果是1，则继续叠加
            if nums[i] == 1:
                tmp += 1
                result = max(result, tmp)
            # 如果是0，初始化
            else:
                tmp = 0

        return result


class Solution2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        双指针写法，遇到1并且没有找到起点的时候就移动左指针，之后遇到1并且找到起点，就一直更新最长长度，直到遇到0，此时起点指针变成false
        """
        first_flag = False
        left = 0
        result = 0

        for i in range(len(nums)):
            # 遇到1，并且没有起点
            if nums[i] == 1 and first_flag is False:
                left = i
                first_flag = True
            # 遇到1并且有起点
            if nums[i] == 1 and first_flag:
                result = max(result, i - left + 1)
            # 遇到0，并且有起点，说明可以结束起点，开始新的起点
            if nums[i] == 0 and first_flag:
                first_flag = False

        return result


s = Solution2()
print(s.findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))
