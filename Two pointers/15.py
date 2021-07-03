def threeSum(nums: [int]) -> [[int]]:
    """
    O(n ^ 2) time，双指针
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
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while right > left and nums[right] == nums[right - 1]:
                    right -= 1
                while right > left and nums[left] == nums[left + 1]:
                    left += 1

                # 找到答案时，双指针同时收缩
                right -= 1
                left += 1

    return result


print(threeSum([1, 2, 3, 4, -1, -2]))