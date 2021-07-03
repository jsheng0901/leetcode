class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        """双指针版本的two sum，左右指针判断每次大小来移动指针"""
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
