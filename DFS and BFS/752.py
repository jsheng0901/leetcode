from typing import List


class Solution:
    def plus_one(self, s: str, j: int) -> str:
        """
        将 s[j] 向上拨动一次
        """

        ch = list(s)

        if ch[j] == '9':
            ch[j] = '0'
        else:
            ch[j] = chr(ord(ch[j]) + 1)

        return ''.join(ch)

    def minus_one(self, s: str, j: int) -> str:
        """
        将 s[j] 向下拨动一次
        """

        ch = list(s)

        if ch[j] == '0':
            ch[j] = '9'
        else:
            ch[j] = chr(ord(ch[j]) - 1)

        return ''.join(ch)

    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Time O(n)
        Space O(n)
        BFS写法，找最短路径都是BFS。构建visited存储访问过的节点，注意构建成set，方便快速查找。
        """
        # 转化成set，记录需要跳过的死亡密码
        deadends_set = set(deadends)

        # 初始化列队和visited，记录已经穷举过的密码，防止走回头路
        queue = []
        visited = set()

        # 注意检查是否起始点就是dead
        # 从起点开始启动广度优先搜索
        if "0000" not in deadends_set:
            queue.append("0000")
            visited.add("0000")

        # 初始化步骤
        step = 0

        while queue:
            size = len(queue)
            # 遍历此层，将当前队列中的所有节点向周围扩散
            for _ in range(size):
                # 当前节点
                num = queue.pop(0)

                # 判断是否到达终点，遇到目的地，直接返回
                if num == target:
                    return step

                # 遍历所有符合的邻居节点及密码，将一个节点的未遍历相邻节点加入队列和访问表
                for j in range(4):
                    #
                    up = self.plus_one(num, j)
                    down = self.minus_one(num, j)
                    if up not in deadends_set and up not in visited:
                        visited.add(up)
                        queue.append(up)
                    if down not in deadends_set and down not in visited:
                        visited.add(down)
                        queue.append(down)

            # 走完了同一层，在这里增加步数
            step += 1

        # 如果穷举完都没找到目标密码，那就是找不到了
        return -1


s = Solution()
print(s.openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
