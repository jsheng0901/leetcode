def minSubArrayLen_0(target: int, nums: [int]) -> int:
    """
    O(n ^ 2) two for loop find all combination of subset

    暴力解法， 两次loop找到所有组合如果长度比之前的小就更新结果, 需要注意的是自己也可以作为一个单一元素测试超过target
    """
    result = float('inf')
    for i in range(len(nums)):
        sum_list = 0
        for j in range(i, len(nums)):
            sum_list += nums[j]
            if sum_list >= target:
                sub_length = j - i + 1
                result = sub_length if sub_length < result else result
                break

    return 0 if result == float('inf') else result


def minSubArrayLen_1(target: int, nums: [int]) -> int:
    """
    O(n) time two pointers,

    双指针及滑动窗口解法， 每次j指针往前走，计算i指针和j直接的距离和总和，如果大于target，就记录下来并且移动i指针往前走一个
    """
    result = float('inf')
    i = 0
    sum_list = 0
    for j in range(len(nums)):
        sum_list += nums[j]
        while sum_list >= target:
            sub_length = j - i + 1
            result = sub_length if sub_length < result else result
            sum_list -= nums[i]
            i += 1

    return 0 if result == float('inf') else result


print(minSubArrayLen_1(7, [2, 3, 1, 2, 4, 3]))
