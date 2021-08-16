class Solution:
    def findBuildings(self, heights: [int]) -> [int]:
        """
        O(n) time, space O(n)
        从右向左遍历，如果有当前一个大于目前的最高build，则加入result，最后reverse result， 但需要reverse
        """
        cur_max = float('-inf')

        result = []

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > cur_max:
                result.append(i)
            cur_max = max(cur_max, heights[i])

        result.reverse()
        # result = self.reverse(result)

        return result

