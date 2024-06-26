from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time O(n * log(n) + n ^ 2)
        Space O(log(n)) sorting 需要
        三指针，先sorting一下保证从小到大搜索，固定一个指针之后双指针从左右开始遍历寻找。注意去重逻辑见注释。
        """
        result = []
        # 找出a + b + c = 0
        # a = nums[i], b = nums[left], c = nums[right]
        # sort nums first，这样保证顺序可以放心移动双指针
        nums.sort()
        for i in range(len(nums)):
            # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
            if nums[i] > 0:
                return result
            # 正确去重方法
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while right > left:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 去重逻辑应该放在找到一个三元组之后，当右边指针大于左边指针的时候进行去重，不然会漏掉0 0 0 这种特殊情况
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    # 找到答案时，双指针同时收缩
                    right -= 1
                    left += 1

        return result


s = Solution()
print(s.threeSum([1, 2, 3, 4, -1, -2]))
