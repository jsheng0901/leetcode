class Solution:
    def search(self, nums: [int], target: int) -> bool:
        """
        same as no repeated number 33, when face nums[mid] == nums[left], just let left ++ and continues
        :param nums:
        :param target:
        :return: 
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[left]:
                left += 1
                continue

            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid] or target < nums[left]:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                elif target < nums[mid] or target > nums[right]:
                    right = mid - 1

        return False

