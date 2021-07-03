class Solution:
    def findContentChildren(self, g: [int], s: [int]) -> int:
        """
        time: O(nlogn) + O(n) = O(nlogn)
        贪心算法的应用，满足每个局部的最优，则满足全局的最优,
        先排序，然后从后向前loop，找到符合条件的小孩
        :param g:
        :param s:
        :return:
        """
        g.sort()
        s.sort()

        index = len(s) - 1
        result = 0
        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                result += 1
                index -= 1

        return result


s = Solution()
print(s.findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8]))
