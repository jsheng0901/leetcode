# 2024-05-13
# Amazon Web Services (AWS) is a cloud computing platform with multiple servers. One of the servers is assigned to
# serve customer requests. There are n customer requests placed sequentially in a queue, where the ith request has a
# maximum waiting time denoted by wait[i]. That is, if the ith request is not served within wait[i] seconds,
# then the request expires, and it is removed from the queue. The server processes the request following the First In
# First Out (FIFO) principle. The 1st request is processed first, and the nth request is served last. At each second,
# the first request in the queue is processed. At the next second, the processed request and any expired requests are
# removed from the queue.
#
# Given the maximum waiting time of each request denoted by the array wait, find the number of requests present in
# the queue at every second until it is empty.
#
# Note:
#
# If a request is served at some time instant t, it will be counted for that instant and is removed at the next
# instant. The first request is processed at time = 0. A request expires without being processed when time = wait[i].
# It must be processed while time < wait[i]. The initial queue represents all requests at time = 0 in the order they
# must be processed. Function Description
#
# Complete the function findRequestsInQueue in the editor.
#
# findRequestsInQueue has the following parameter:
#
# int wait[n]: the maximum waiting time of each request
# Returns
#
# int[]: the number of requests in the queue at each instant until the queue becomes empty.
from typing import List


class Solution:
    def findRequestsInQueue(self, wait: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        先存记录所有在每个时间段expire的serve的个数，之后遍历所有queue里面的serve，先记录当前serve的个数，更新当前serve的个数，包括
        当前正在serve的这个和expired的时间段对应的个数。注意这里一定要更新expiration里面当前serve的这个个数，不然后续统计的时候，会出现
        把之前已经serve过的又减一次的情况。详细见注释。
        """
        expirations = [0] * (10 ** 5)
        # 记录同一个时间expire的个数
        for i in range(len(wait)):
            expirations[wait[i]] += 1

        # 统计当前还剩多少要serve
        cur_request = len(wait)
        # 当前时间
        time = 0
        # 记录结果
        res = []
        for i in range(len(wait)):
            if wait[i] >= time:
                # 注意这里的每一条顺序，都不能改
                # 当前在queue的serve的个数，加入结果
                res.append(cur_request)
                # if
                # 更新当前正在被serve的这个对应的expire时间的个数
                expirations[wait[i]] -= 1
                # 当前serve了一个，所以 -1
                cur_request -= 1
                # 减掉当前时间下会expire的serve的个数
                expired_requests = expirations[time + 1]
                if expired_requests > 0:
                    cur_request -= expirations[time + 1]
                    expirations[time + 1] = 0

                # 时间 +1
                time += 1

            # 如果全部serve完，直接结束，这一步很重要，否则会出现负数加入结果
            if cur_request <= 0:
                break

        # 最终添加一个0，因为移除正在serve的这个在下一个time，所以一定会有0在最后，表示全部serve完，
        res.append(0)
        return res


import heapq


def check(wait):
    res = []
    heap = wait[:]
    heapq.heapify(heap)
    max_wait = max(wait)
    t = 0
    i = 0
    while i <= len(wait) and heap:

        if t + 1 == wait[0]:
            heapq.heappop(heap)
            i += 1
        res.append(len(heap))

        t += 1
        while heap and t + 1 > heap[0]:
            heapq.heappop(heap)

    while t <= max_wait:
        res.append(0)
        t += 1

    return res


class Solution2:
    def findRequestsInQueue(self, wait: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        先存记录所有在每个时间段expire的serve的个数，之后遍历所有queue里面的serve，先记录当前serve的个数，更新当前serve的个数，包括
        当前正在serve的这个和expired的时间段对应的个数。注意这里一定要更新expiration里面当前serve的这个个数，不然后续统计的时候，会出现
        把之前已经serve过的又减一次的情况。详细见注释。
        """
        expirations = [0] * (10 ** 5)
        # 记录同一个时间expire的个数
        for i in range(len(wait)):
            expirations[wait[i]] += 1

        # 统计当前还剩多少要serve
        cur_request = len(wait)
        # 当前时间
        time = 0
        # 记录结果
        res = []
        for i in range(len(wait)):
            if wait[i] >= time:
                # 注意这里的每一条顺序，都不能改
                # 当前在queue的serve的个数，加入结果
                res.append(cur_request)
                # if
                # 更新当前正在被serve的这个对应的expire时间的个数
                expirations[wait[i]] -= 1
                # 当前serve了一个，所以 -1
                cur_request -= 1
                # 减掉当前时间下会expire的serve的个数
                expired_requests = expirations[time + 1]
                if expired_requests > 0:
                    cur_request -= expirations[time + 1]
                    expirations[time + 1] = 0

                # 时间 +1
                time += 1

            # 如果全部serve完，直接结束，这一步很重要，否则会出现负数加入结果
            if cur_request <= 0:
                break

        # 最终添加一个0，因为移除正在serve的这个在下一个time，所以一定会有0在最后，表示全部serve完，
        res.append(0)
        return res


print(check([3, 1, 2, 1]))

# s = Solution()
# print(s.findRequestsInQueue(wait=[2, 2, 3, 1]))
# print(s.findRequestsInQueue(wait=[4, 4, 4]))
# print(s.findRequestsInQueue(wait=[3, 1, 2, 1]))
