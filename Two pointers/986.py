class Solution:
    def intervalIntersection(self, firstList: [[int]], secondList: [[int]]) -> [[int]]:
        """
        Time O(n)
        Space O(n)
        双指针，找每一次上下对应的最大左边和最小右边值，当最大左小于等于最小右的时候说明有交集，直接加入结果。
        当一个最小右值小于另一个的最小右值时候，说明此区间已经被检查过是否有交集，则抛弃这个跳到下一个区间。
        """
        ans = []
        i = 0
        j = 0

        # 如果一边先走完，说明后面一定不会有交集，说明两个都要在范围内才有交集
        while i < len(firstList) and j < len(secondList):
            # 最大左边值
            left = max(firstList[i][0], secondList[j][0])
            # 最小右边值
            right = min(firstList[i][1], secondList[j][1])

            # 出现交集
            if left <= right:
                ans.append([left, right])

            # 检查是否要跳到下一个区间
            if firstList[i][1] < secondList[j][1]:  # 进入下一个interval
                i += 1
            else:
                j += 1

        return ans


s = Solution()
print(s.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                             secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))
