class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        """
        数组和hash table的结合应用，典型的空间换时间
        先存储所有数进入set,当找到一个数的前一个不在set里面的时候就从现在这个数开始向前+1进行while loop找下一个数在不在set里面
        如果在就记录当前距离，直到不在set里面就比较当前距离和最长距离，并更新最长距离
        """
        if len(nums) == 0:
            return 0

        long = 0
        m = set()
        for i in nums:
            m.add(i)

        for j in range(len(nums)):
            if nums[j] - 1 not in m:
                cur = nums[j]
                cur_length = 1
                while cur + 1 in m:
                    cur_length += 1
                    cur += 1
                long = max(long, cur_length)

        return long



