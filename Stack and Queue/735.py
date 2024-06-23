from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        用栈来记录每次进来的小行星和当前栈顶的小行星，然后对比是否会相撞并且撞的情况，详细见注释，此题的难点是理清楚撞的情况和撞后的情况。
        """
        stack = []
        # 遍历每个小行星
        for asteroid in asteroids:
            # 如果栈顶有元素，并且方向相反，则一定会相撞，注意这里是while loop，因为可能当前小行星一直撞到栈底
            while stack and stack[-1] > 0 > asteroid:
                # case1：当前小行星大于栈顶小行星，栈顶小行星被撞掉
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    # 注意这里要用continue，持续loop判断下一个栈顶小行星
                    continue
                # case2：当前小行星等于栈顶小行星，栈顶小行星被撞掉，同时当前小行星也被撞掉
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()

                # case3：当前小行星小于栈顶小行星，当前小行星被撞掉
                # 除去第一种情况，其它两种情况，都不再需要继续loop，所以一定会走到break
                # 另外两种情况当前小行星都不需要入栈，因为都会被撞掉
                break
            # 用一个loop else来接住，当没loop有走到break就结束循环的时候，也就是如果一直是第一种情况到跳出loop，基本上就是当前小行星
            # 比栈内所有小行星都大并且方向都相反，则当前小行星一定要入栈。
            else:
                stack.append(asteroid)

        # 返回栈内剩余的小行星就是结果
        return stack


s = Solution()
print(s.asteroidCollision(asteroids=[5, 10, -5]))
print(s.asteroidCollision(asteroids=[8, -8]))
print(s.asteroidCollision(asteroids=[10, 2, -5]))
