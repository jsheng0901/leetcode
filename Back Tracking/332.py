from collections import defaultdict
from typing import List


class Solution1:
    def __init__(self):
        # target 记录 {出发机场, {到达机场, 航班次数}}
        self.result = []
        self.targets = {}

    def backtracking(self, ticket_number):
        if len(self.result) == ticket_number + 1:
            return True

        if self.result[-1] in self.targets:  # 判断是否存在这个出发地，最终目的的是没有在对应的出发地的，否则会报错
            for k in sorted(self.targets[self.result[-1]]):
                # 每次loop的是当前出发地对应的目的地, 这里一定要先sort，否则输出顺序不对
                # 要保证输出的每个出发地对应目的地在dictionary里面的顺序，字母小的在前面
                value = self.targets[self.result[-1]][k]
                if value > 0:
                    self.result.append(k)
                    self.targets[self.result[-2]][k] -= 1
                    if self.backtracking(ticket_number):
                        return True
                    # self.result = self.result[:len(self.result) - 1]
                    # self.targets[self.result[-1]][k] += 1
                    # 也可以先更新递归后回溯的value值，则此时依旧是index -2，然后pop out上一个加入result的起飞地，此处可以直接用pop
                    self.targets[self.result[-2]][k] += 1
                    self.result.pop()
        else:
            return False

    def findItinerary(self, tickets: [[str]]) -> [str]:
        """
        Time O(nlog(n)) 搜索一条path并且sort
        Space O(n)
        深度搜索题型包含回溯在内，遍历整棵树找到符合条件的某一条树枝路径。回溯题目处理当前节点一般在for loop里面，因为回溯关注的是
        当前节点到下一个节点的树枝，而graph里面的DFS一般处理当前节点再loop外，因为graph关注的是当前节点。
        """
        # 记录映射关系
        for i in tickets:
            if i[0] not in self.targets:
                self.targets[i[0]] = {i[1]: 1}
            else:
                if i[1] in self.targets[i[0]]:
                    self.targets[i[0]][i[1]] += 1
                else:
                    self.targets[i[0]][i[1]] = 1

        self.result.append("JFK")  # 起始机场

        self.backtracking(len(tickets))

        return self.result


class Solution2:
    def __init__(self):
        self.result = []

    def dfs(self, airport, graph):

        # 递归终止条件是当此机场目的地不存在的时候
        dst_list = graph[airport]
        while dst_list:
            # 弹出下一个机场，并进入递归
            next_src = dst_list.pop(0)
            self.dfs(next_src, graph)
        # 找到最终没有目的地的机场，及终点，然后我们加入最终list，需要注意是此处是后续遍历的顺序加入。
        self.result.append(airport)

        return

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Time O(nlog(n)) 搜索一条path并且sort
        Space O(n)
        与第一种方法不一样的前序遍历的思路，类似后续遍历的思路，找到valid的path再开始从底向上开始记录整个path进过的点，最后翻转一下结果即可
        此方法不一样地方还有一直update目的地list，这样才可以找到最终没有目的地的机场。
        """
        graph = defaultdict(list)
        for src, dst in sorted(tickets):
            graph[src].append(dst)

        self.dfs("JFK", graph)

        return self.result[::-1]


s = Solution2()
print(s.findItinerary(tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
