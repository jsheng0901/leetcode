# 2024-05-10
# Developers at Amazon have deployed an application with a distributed database. It is stored on total_servers
# different servers numbered from 1 to total_servers that are connected in a circular fashion, i.e. 1 is connected to
# 2, 2 is connected to 3, and so on until total_servers connects back to 1.
#
# There is a subset of servers represented by an array servers of integers. They need to transfer the data to each
# other to be synchronized. Data transfer from one server to one it is directly connected to takes 1 unit of time.
# Starting from any server, find the minimum amount of time to transfer the data to all the other servers.
#
# Function Description
#
# Complete the function getMinTime in the editor.
#
# getMinTime takes the following arguments:
#
# int total_servers: The number of servers in the system
# int servers[n]: The servers to share the data with
# Returns
#
# int: The minimum time required to transfer the data on all the servers
from typing import List


class Solution:
    def getMinTime(self, total_servers: int, servers: List[int]) -> int:
        """
        Time O(n * log(n) + n)
        Space O(1)
        此题非常巧妙，先sort一下，这样每次都是从当前点走到尾巴的点，保证只需要计算一次得出总路程。其次下一个巧妙的地方在于得到下一个点的index，
        这里需要引入余数的概念，详细见注释。
        """
        # 先从小到大排序
        servers.sort()
        n = len(servers)
        res = float('inf')
        # 遍历每个点作为起点，计算最短的距离和
        for i in range(n):
            # 起始点
            from_server = servers[i]
            # 终点，这里终点就是起点的前面一个点或者，如果是第一个点，终点就是最后一个点，如果是最后一个点，终点就是第一个点。
            to_server = servers[(i + n - 1) % n]

            # 正常顺序，直接相减计算
            if from_server < to_server:
                res = min(res, to_server - from_server)
            # 遇到循环的路线，需要先计算正常顺序再用总路径相减
            else:
                res = min(res, total_servers - (from_server - to_server))

        return res


s = Solution()
print(s.getMinTime(total_servers=8, servers=[2, 6, 8]))
print(s.getMinTime(total_servers=5, servers=[1, 5]))
print(s.getMinTime(total_servers=10, servers=[4, 6, 2, 9]))
