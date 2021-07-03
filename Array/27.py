def removeElement(nums: [int], val: int) -> int:
    """
    O(n)  time loop once with two pointers

    当慢指针和快指针指向同一个不等于value的元素时候，一起向前进一步，
    当快指针指向等于value的元素时候，慢指针不动，快指针继续，直到找到下一个不一样的，然后与慢指针相互交换位置，同时慢指针向前走一步
    这里慢指针会停下来一定是找到了一个等于value的数值，并且会刚好停在这个数前一个index处
    """
    slow_index = 0
    for fast_index in range(len(nums)):
        if val != nums[fast_index]:
            nums[slow_index] = nums[fast_index]  # 快慢指针相互交换位置
            slow_index += 1  # 慢指针向前走一步

    return slow_index


index = removeElement([1, 2, 3, 4, 5, 3, 3], 3)
print(index)
