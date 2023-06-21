
def search_insert_0(nums: [int], target: int) -> int:
    """
    time O(n) loop nums once
    space O(1)
    """
    for i in range(len(nums)):
        if nums[i] >= target:
            return i

    return len(nums)


def search_insert_1(nums: [int], target: int) -> int:
    """
    time O(logn) binary search time
    space O(1)
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

    return right + 1    # or just return left


index = search_insert_1([1, 2, 3, 4], 5)
print(index)
