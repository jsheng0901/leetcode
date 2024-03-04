from typing import List


class Solution1:
    def numFriendRequests(self, ages: List[int]) -> int:
        """
        Time O(n^2)
        Space O(1)
        双循环，暴力解法，TLE明显。
        """
        request = 0
        for i in range(len(ages)):
            for j in range(len(ages)):
                if i == j:
                    continue
                if ages[j] <= ages[i] * 0.5 + 7:
                    continue
                if ages[j] > ages[i]:
                    continue
                if ages[j] > 100 > ages[i]:
                    continue
                request += 1

        return request


class Solution2:
    def right_bound(self, nums, target) -> int:
        # 这里是找右边界的模版
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
        # 区别在这里，我们返回是大于右边界的第一个数的index，而不是右边界，跳出while loop的条件是 right = left - 1
        # 所以我们需要的是right + 1 也就是 left index
        return left

    def numFriendRequests(self, ages: List[int]) -> int:
        """
        Time O(n * log(n) + log(n) + log(n-1) + log(n-2) ... + log(1))
        Space O(1)
        先sort一遍，因为只加比自己小的人，所以从后往前遍历，因为是有序的所以我们可以用二分法找到边界，这里要找的是第一个或者说最小的比target
        值大的index，所以应该是找right bound，返回边界 +1，之后直接index计算中间有多少个数。这里有个edge case是当数字是相等的时候，
        并不需要重新找边界，当前边界等于上一个相等的数字的结果。
        """
        request = 0
        ages.sort()
        total_requests = 0

        for i in range(len(ages) - 1, -1, -1):
            target = ages[i] * 0.5 + 7
            # 当target大于数字的时候，因为是递减的顺序遍历，直接跳过后面的所有数字可以
            if target > ages[i]:
                break
            # trick这里，当前和上一个相等的情况，request数量和之前的一样应该，同时跳过这个数不用从新找边界
            if i < len(ages) - 1 and ages[i] == ages[i + 1]:
                total_requests += request
                continue
            # 找右边界
            right_index = self.right_bound(ages[:i], target)
            # 计算有多少个数字中间
            request = i - right_index
            total_requests += request

        return total_requests


s = Solution2()
print(s.numFriendRequests(ages=[16, 16]))
print(s.numFriendRequests(ages=[16, 17, 18]))
print(s.numFriendRequests(ages=[20, 30, 100, 110, 120]))
print(s.numFriendRequests(ages=[101, 56, 69, 48, 30]))
print(s.numFriendRequests(ages=[108, 115, 5, 24, 82]))
print(s.numFriendRequests(ages=[73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]))
print(s.numFriendRequests(
    ages=[98, 60, 24, 89, 84, 51, 61, 96, 108, 87, 68, 29, 14, 11, 13, 50, 13, 104, 57, 8, 57, 111, 92, 87, 9, 59, 65,
          116, 56, 39, 55, 11, 21, 105, 57, 36, 48, 93, 20, 94, 35, 68, 64, 41, 37, 11, 50, 47, 8, 9]))
