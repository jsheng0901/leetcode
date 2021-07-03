
def search_insert_0(nums: [int], target: int) -> int:
    """
    O(n) loop nums once
    """
    for i in range(len(nums)):
        if nums[i] >= target:
            return i

    return len(nums)


def search_insert_1(nums: [int], target: int) -> int:
    """
    O(logn) binary search time
    """
    left = 0
    right = len(nums) - 1   # 定义target在左闭右闭的区间里，[left, right]
    while left <= right:    # when left equal right, target value can same as middle
        middle = left + (right - left) // 2
        if nums[middle] < target:   # target on right side
            left = middle + 1
        elif nums[middle] > target:     # target on left side, right as middle - 1 because 区间是可以两边取到的
            right = middle - 1
        else:
            return middle

    return right + 1


index = search_insert_1([1, 2, 3, 4], 5)
print(index)
