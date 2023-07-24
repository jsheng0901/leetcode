class Solution:
    def __init__(self):
        # target 记录 {出发机场, {到达机场, 航班次数}}
        self.result = []
        self.targets = {}

    def backtracking(self, ticket_number):
        if len(self.result) == ticket_number + 1:
            return True

        if self.result[-1] in self.targets:             # 判断是否存在这个出发地，最终目的的是没有在对应的出发地的，否则会报错
            for k in sorted(self.targets[self.result[-1]]):
                # 每次loop的是当前出发地对应的目的地, 这里一定要先sort，否则输出顺序不对
                # 要保证输出的每个出发地对应目的地在dictionary里面的顺序，字母小的在前面
                value = self.targets[self.result[-1]][k]
                if value > 0:
                    self.result.append(k)
                    self.targets[self.result[-2]][k] -= 1
                    if self.backtracking(ticket_number):
                        return True
                    self.result = self.result[:len(self.result) - 1]
                    self.targets[self.result[-1]][k] += 1
        else:
            return False

    def findItinerary(self, tickets: [[str]]) -> [str]:
        """
        深度搜索题型包含回溯在内，遍历整棵树找到符合条件的某一条树枝路径
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


s = Solution()
print(s.findItinerary(tickets=[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
