# 2024-05-02
# magine you are shopping on Amazon.com for some good weight lifting equipment. The equipment you want has blocks of
# many different weights that you can combine to lift.
#
# The listing on Amazon gives you an array, blocks, that consists of n different weighted blocks, in kilograms. There
# are no two blocks with the same weight. The element blocks[i] denotes the weight of the ith block from the top of
# the stack. You consider weight lifting equipment to be good if the block at the top is the lightest, and the block
# at the bottom is the heaviest.
#
# More formally, the equipment with array blocks will be called good weight lifting equipment if it satisfies the
# following conditions assuming the index of the array starts from 1:
#
# blocks[1] < blocks[i] for all 2 ≤ i ≤ n blocks[i] < blocks[n] for all 1 ≤ i ≤ n-1 In one move, you can swap the
# order of adjacent blocks. Find out the minimum number of moves required to form good weight lifting equipment.
#
# Function Description
#
# Complete the function getMinNumMoves in the editor.
#
# getMinNumMoves has the following parameter:
#
# int blocks[n]: the distinct weights
# Returns
#
# int: the minimum number of operations required
from typing import List


class Solution:
    def getMinNumMoves(self, blocks: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        同2340，基本上就是找到最大最小值的index，然后两种情况，第一种最小在最大左边，那就直接swap次数叠加，第二种有交集，叠加后 -1。
        """
        max_index = 0
        max_value = float('-inf')
        min_index = 0
        min_value = float('inf')
        # 找最大最小值的index
        for i, v in enumerate(blocks):
            if v >= max_value:
                max_value = v
                max_index = i
            if v < min_value:
                min_value = v
                min_index = i

        # 分别计算到最后和开头swap的次数
        max_swap = len(blocks) - 1 - max_index
        min_swap = min_index - 0
        # 情况1，没有交集，直接叠加
        if max_index >= min_index:
            return max_swap + min_swap
        # 情况2，有交集，少一步
        else:
            return max_swap + min_swap - 1


s = Solution()
print(s.getMinNumMoves(blocks=[2, 4, 3, 1, 6]))
print(s.getMinNumMoves(blocks=[4, 11, 9, 10, 12]))
print(s.getMinNumMoves(blocks=[3, 2, 1]))
