from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Time O(n)
        Space O(n)
        hash table也就是构建graph的使用。我们只需要找到一个点，没有出度，但是入度等于 n - 1，除自己以外都指向过自己。
        构建graph的时候计算每个点被指向的次数，然后遍历一下count数组即可。
        """
        graph = defaultdict(list)
        # 记录每个点被访问的次数，及入度
        count = [0] * (n + 1)
        for edge in trust:
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            # 被访问过则 +1
            count[node2] += 1

        # 找到一个点没有出度，及没有在graph hash table内，并且入度为 n - 1，返回结果
        for i in range(1, len(count)):
            if i not in graph and count[i] == n - 1:
                return i

        return -1


s = Solution()
print(s.findJudge(n=3, trust=[[1, 2], [2, 3]]))
print(s.findJudge(n=2, trust=[[1, 2]]))
print(s.findJudge(n=3, trust=[[1, 3], [2, 3]]))
print(s.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
