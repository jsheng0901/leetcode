def fourSum(nums: [int], target: int) -> [[int]]:
    """
    O(n ^ 3) time, 思路和三数之后一样，区别是三数是两层loop，四数是三层loop
    """
    result = []
    # 找出a + b + c + d = target
    # a = nums[i], b = nums[j], c = nums[left], d = nums[right]
    # sort nums first，这样保证顺序可以放心移动双指针
    nums.sort()
    for i in range(len(nums)):
        # 正确去重方法
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i+1, len(nums)):
            # 正确去重方法，此处记得往前跳一个测试是否相同，及k比i多两个index的时候查重
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] > target:
                    right -= 1
                elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    result.append([nums[i], + nums[j], nums[left], nums[right]])
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1

    return result


print(fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
