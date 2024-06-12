from typing import List


class Solution1:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        构建前缀和，这里比较巧妙的是，0，1可以转化成 -1 和 1，这样如果balance的话这个区间的和应该是0，
        之后用字典存储每个值对应的index，如果出现过一样的说明在两个一样的数的区间内存在balance数组，找出长度，更新最大值。这里有个特例是
        当遇到0的时候，其实距离原点就是最大值，所以字典里面要初始化一个{0: -1}的pair。
        """
        # 构建前缀和
        pre_sum = []
        if nums[0] == 0:
            pre_sum.append(-1)
        else:
            pre_sum.append(1)

        for i in range(1, len(nums)):
            val = -1 if nums[i] == 0 else 1
            pre_sum.append(pre_sum[i - 1] + val)
        # 初始化字典
        hash_map = {0: -1}
        max_length = float('-inf')
        # 遍历前缀和
        for i, v in enumerate(pre_sum):
            # 如果没有出现过，记录下来index
            if v not in hash_map:
                hash_map[v] = i
            # 如果出现过，这里是计算length的核心，出现同样的数的index1，和index2，[index1 + 1: index2]其实才是balance的区间，
            # 这里计算长度，刚好应该是 index2 - (index1 + 1) + 1 == index2 - index1，也就是相同数的index相减
            # 再因为这里是向前loop，所以找到相同数的顺序就是对应的最大值出现的顺序，并不需要更新相同数的index。
            else:
                max_length = max(max_length, i - hash_map[v])

        # 有可能不存在这样的区间，返回0
        return 0 if max_length == float('-inf') else max_length


class Solution2:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        同样的思路，不过这里只需要遍历一次，其实更快。把前缀和的计算过程融合进去一起算。因为我们并不需要保存整个前缀和，只需要一个指针，
        一直记录当前的和即可。因为是一直向前loop，走过的部分可以不需要记录下来。
        """
        # 前缀和指针
        pre_sum = 0
        hash_map = {0: -1}
        max_length = float('-inf')
        for i in range(len(nums)):
            # 计算走到当前位置的前缀和
            pre_sum += -1 if nums[i] == 0 else 1
            # 之后部分同思路1
            if pre_sum not in hash_map:
                hash_map[pre_sum] = i
            else:
                max_length = max(max_length, i - hash_map[pre_sum])

        return 0 if max_length == float('-inf') else max_length


s = Solution2()
print(s.findMaxLength(nums=[0, 1]))
print(s.findMaxLength(nums=[0, 1, 1]))
print(s.findMaxLength(nums=[0, 1, 0]))
print(s.findMaxLength(nums=[0, 1, 0, 1]))
print(s.findMaxLength(nums=[0, 0, 1, 0, 0, 0, 1, 1]))
