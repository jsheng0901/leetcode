class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        """three sum template just go through all combination and check difference"""
        nums.sort()

        min_diff = float('inf')
        result = float('inf')

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                cur_diff = abs(cur_sum - target)
                if cur_diff < min_diff:
                    min_diff = cur_diff
                    result = cur_sum

                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
                elif cur_sum == target:
                    return target
                #
                # while left < right and nums[left] == nums[left - 1]:
                #     left += 1
                # while left < right and nums[right] == nums[right - 1]:
                #     right -= 1

        return result


s = Solution()
print(s.threeSumClosest(nums=[0, 2, 1, -3], target=1))
