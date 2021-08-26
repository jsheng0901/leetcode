class Solution:
    def intervalIntersection(self, firstList: [[int]], secondList: [[int]]) -> [[int]]:
        """双指针，找每一次上下对应的最左边和最右边值，当一个最右值小于另一个的时候抛弃这个跳到下一个"""
        ans = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])

            if left <= right:
                ans.append([left, right])

            if firstList[i][1] < secondList[j][1]:      # 进入下一个interval
                i += 1
            else:
                j += 1

        return ans


