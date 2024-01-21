from typing import List


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


class Solution2:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Time O(n)
        Space O(n)
        一样的思路，只是判断交集的方式不一样，当下面的右大于上面的左，下面的左小于上面的右的时候一定有交集。
        交集只有四种情况：
            1. a: [2, 5] b: [1, 7]
            2. a: [2, 5] b: [4, 7]
            3. a: [2, 5] b: [3, 4]
            4. a: [2, 5] b: [1, 4]
        计算交集保留最大左边和最小右边。之后check下一个区间
        """
        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i][0], firstList[i][1]
            b1, b2 = secondList[j][0], secondList[j][1]

            if b2 >= a1 and a2 >= b1:
                res.append([max(a1, b1), min(a2, b2)])

            if b2 < a2:
                j += 1
            else:
                i += 1

        return res


class Solution3:
    def intervalUnion(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Time O(n)
        Space O(n)
        一样的思路，这里改成计算并集。首先还是四种情况计算是否有交集，如果有此时保留最小左和最大右。
        每次union后要更新大的那个list的对应的元素为union后的值，这样才可以一直union，并用一个tmp指针记录union值，如果没有交集的时候，
        说明union结束，tmp如果存在则加入结果，如果不存在说明，一开始就没有union结果，此时就把小的那个list直接加入结果。然后继续遍历。
        这里需要判断一下最后tmp是否还有值，因为可能最后union完没有下一个指针判断会直接跳出loop，此时tmp如果还有值说明是最后一个union，
        则直接加入结果。
        """
        res = []
        i, j = 0, 0
        # 特殊情况
        if len(firstList) > 0 and len(secondList) == 0:
            for el in firstList:
                res.append(el)
        if len(firstList) == 0 and len(secondList) > 0:
            for el in secondList:
                res.append(el)

        tmp = None
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i][0], firstList[i][1]
            b1, b2 = secondList[j][0], secondList[j][1]

            # 如果有交集
            if b2 >= a1 and a2 >= b1:
                # 记录交集的结果
                tmp = [min(a1, b1), max(a2, b2)]
                # 判断那个list要更新交集过后的结果
                if b2 < a2:
                    firstList[i] = [min(a1, b1), max(a2, b2)]
                    j += 1
                else:
                    secondList[j] = [min(a1, b1), max(a2, b2)]
                    i += 1
            # 没有交集
            else:
                # 存在之前计算过的交集，加入结果
                if tmp is not None:
                    res.append(tmp)
                # 不存在，说明一直没有交集
                else:
                    # 判断一下哪个list加入结果
                    if b1 > a2:
                        res.append([a1, a2])
                    else:
                        res.append([b1, b2])
                # 判断一下指针一定
                if b2 < a2:
                    j += 1
                else:
                    i += 1

        # check最后是否还存在一个最后的union没有加入
        if tmp:
            res.append(tmp)

        return res


s = Solution2()
print(s.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                             secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))

s = Solution3()
print(s.intervalUnion(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                      secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))
print(s.intervalUnion(firstList=[[1, 3], [5, 9]], secondList=[]))
print(s.intervalUnion(firstList=[[1, 3], [5, 9]], secondList=[[2, 5], [7, 10]]))
print(s.intervalUnion(firstList=[[1, 3], [5, 9]], secondList=[[0, 0], [2, 3], [7, 10]]))
