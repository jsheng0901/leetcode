from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        本质上是找到一个固定窗口内的最少0的个数的窗口，因为把所有1都放在一起也就是一定需要的窗口大小，此时窗口内的0越少说明需要swap的次数也就
        越少，找到这样一个窗口也就是找到了对应的最少swap次数。剩下的就是滑动窗口的模板题。
        """
        # 计算找到窗口的大小
        window_size = 0
        for val in data:
            if val == 1:
                window_size += 1

        # 左右指针
        left = 0
        right = 0
        # 窗口内0的次数
        window = 0
        # 最少swap次数
        min_swaps = float('inf')
        while right < len(data):
            # 进窗口的数
            c = data[right]
            right += 1
            # 如果是0，累加次数
            if c == 0:
                window += 1

            # 如果超过窗口
            if right - left == window_size:
                # 此时需要记录最小次数
                min_swaps = min(min_swaps, window)
                # 弹出的数
                d = data[left]
                left += 1
                # 如是0，相对应的减少次数
                if d == 0:
                    window -= 1

        # 如果完全没有1，整个数组里面，直接返回0
        return 0 if min_swaps == float('inf') else min_swaps


s = Solution()
print(s.minSwaps(data=[1, 0, 1, 0, 1]))
print(s.minSwaps(data=[0, 0, 0, 1, 0]))
print(s.minSwaps(data=[1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))
