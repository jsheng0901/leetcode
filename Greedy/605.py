from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Time O(n)
        Space O(1)
        对于所有可能放置花的地方我们进行放置花，最后记录最多可以放置花的个数，如果大于等于给定的个数，则返回true。具体如何判断是否可以放置花
        见注释。基本上就是对当前位置判断是否为0并且相邻的后一位不是1，如果是0后一位不是1则放置花。
        """
        flower = 0
        i = 0
        while i < len(flowerbed):
            # 如果是0，并且后一位不是1，说明可以放置花
            if i < len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i + 1] != 1:
                # 计数器 +1
                flower += 1
                # 跳两步
                i += 2
            # 如果是0，并且是最后一位特殊情况，不需要载check后一位了，可以放置花
            elif flowerbed[i] == 0 and i == len(flowerbed) - 1:
                # 计数器 +1
                flower += 1
                # 跳两步或者一步都可以，因为已经走到底了
                i += 2
            # 如果是1，则不能放花，邻居也不能放花，直接跳两步
            elif flowerbed[i] == 1:
                i += 2
            # 其它情况比如是0但是邻居是1，都直接跳1步
            else:
                i += 1

            # 优化如果已经大于题目给定的数，直接返回true结束
            if flower >= n:
                return True

        # 返回判断是否可以满足题目给定的数量
        return flower >= n


s = Solution()
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
