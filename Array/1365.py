class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        """
        O(nlog(n)) time, O(n) space
        构造新的sort后的数组，记录新的数组的数字和index的映射关系，此时只用记录重复数字的第一个index
        然后再次遍历原始数组，找到原始数字对应的sort后的index，这个数字就是最少小于此数字的个数
        """
        result = nums[:]
        mapping = {}
        result.sort()                       # 从小到大排序之后，元素下标就是小于当前数字的数字
        for i, v in enumerate(result):
            if v not in mapping:            # 重复数字不用更新，只记录最左边的
                mapping[v] = i

        for i, v in enumerate(nums):
            result[i] = mapping[v]

        return result

