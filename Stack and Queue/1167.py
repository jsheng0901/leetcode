import heapq


class Solution:
    def connectSticks(self, sticks: [int]) -> int:
        """
        prior queue, min heap,
        O(n log(n)) time: build heap: nlog(n), remove and add log(n) by n - 1 times, overall O(n log(n))
        O(n) space build heap

        always pick smallest two number to combine and calculate sum, can't do sort and loop, because sometimes first
        two sum then add next one may not be smallest two.
        """
        res = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)    # pop top min number
            heapq.heappush(sticks, cost)        # add new cost in heap
            res += cost

        return res

