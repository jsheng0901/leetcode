from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(n)
        此题理解题意最重要，本质上是希望每一次翻起来的牌是从大到小的顺序，所以顺理成章先sort，然后就是考虑然后放入数组。按照题意，
        我们需要的起始是把sort过后的牌按照题目规则的index进行插入结果。所以用一个queue来记录规则下的index。
        """
        # 先sort
        deck.sort()
        # sort过后的原始index入列队
        queue = deque()
        for i in range(len(deck)):
            queue.append(i)
        # 记录结果
        res = [0] * len(deck)
        # 记录哪一个牌的指针
        p = 0

        while queue:
            # 当前牌插入的index
            cur = queue.popleft()
            res[cur] = deck[p]
            # 如果还有下一个牌
            if queue:
                # 按照题意，弹出并且加入到最后一位
                queue.append(queue.popleft())
            # 下一个牌指针
            p += 1

        return res


s = Solution()
print(s.deckRevealedIncreasing(deck=[17, 13, 11, 2, 3, 5, 7]))
