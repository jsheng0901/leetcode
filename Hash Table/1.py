def twoSum(nums: [int], target: int) -> [int]:
    """
    O(n) time, loop over nums and store index in dictionary
    """
    element_index_map = {}
    for i in range(len(nums)):
        rest = target - nums[i]                  # find rest of num
        if rest not in element_index_map:
            element_index_map[nums[i]] = i       # if rest of num not in dict then we store our current num and index
        else:
            return [element_index_map[rest], i]  # if rest in dict, we return index of both


print(twoSum([3, 7, 11, 15], 14))
