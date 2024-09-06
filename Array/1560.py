from typing import List


class Solution1:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        模拟整个马拉松的过程，同时记录每个访问过的点的频率，三种情况需要注意，详细见注释。
        """
        # 记录每个点的访问频率
        count = [0] * (n + 1)

        for i in range(len(rounds) - 1):
            # 如果起点小于终点
            if rounds[i] < rounds[i + 1]:
                # 不用记录终点，因为终点在下一层的起点会被记录
                for idx in range(rounds[i], rounds[i + 1]):
                    count[idx] += 1
            # 如果起点终点一样
            elif rounds[i] == rounds[i + 1]:
                for idx in range(1, n + 1):
                    count[idx] += 1
            # 如果起点大于终点，反向走，逆时针
            else:
                # 先走到最大，再走到终点
                for idx in range(rounds[i], n + 1):
                    count[idx] += 1
                for idx in range(1, rounds[i + 1]):
                    count[idx] += 1

        # 最后一个终点要记录一次
        count[rounds[-1]] += 1
        # 统计最大出现的频率
        res = []
        max_freq = max(count)
        # 找到最大出现的频率并记录下来index
        for i, val in enumerate(count):
            if i == 0:
                continue
            if val == max_freq:
                res.append(i)

        return res


class Solution2:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(1)
        其实此题无论怎么跑，只和终点起点相关，中间的经过点并不重要。
        两种情况：
        终点大于起点，说明终点到起点过程中的点访问次数是一样的，并且是最大的。
        终点小于起点，说明终点到最大点，和最大点到起点的过程访问次数是一样的，并且是最大的。
        """
        start = rounds[0]
        end = rounds[-1]
        # case 1
        if end >= start:
            return [i for i in range(start, end + 1)]
        # case 2
        else:
            # 初始点到终点 + 起点到顶点
            return [i for i in range(1, end + 1)] + [i for i in range(start, n + 1)]


s = Solution2()
print(s.mostVisited(n=4, rounds=[1, 3, 1, 2]))
