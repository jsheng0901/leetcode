class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        """
        Time O(n)   worse case loop走完所有数
        Space O(1)
        双指针版本的two sum，左右指针判断每次大小来移动指针
        """
        left = 0
        right = len(numbers) - 1

        # 不需要等于的情况，左右指针等于的情况下没有意义
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]


s = Solution()
print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
