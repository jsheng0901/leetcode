# 2024-05-10
# A student is preparing for a test from amazon academy for a scholarship.
#
# The student is required to completely read n chapters (which is the length of the pages array) for the test where
# the ith chapter has pages[i] number of pages. The chapters are read in increasing order of the index. Each day the
# student can either read till the end of a chapter or at the most x pages, whichever is minimum. The number of pages
# remaining to read decreases by x in the later case.
#
# Note:
#
# The test will be given in [days] number of days from now. Find the minimum number of the pages, x,
# which the student should read each day to finish all pages of all chapters within days number of days. If it is not
# possible to finish these chapters in days number of days, return -1.
#
# Function Description
#
# Complete the function findMinimumPagesPerDay in the editor.
#
# findMinimumPagesPerDay has the following parameters:
#
# int pages[n]: an array of integers representing the number of pages in each chapter
# int days: the number of days to finish reading
# Returns
#
# int: the minimum number of pages to read each day, or -1 if it's not possible
#
# Note: In one day, the student cannot read pages of more than one chapter. Thus, if a chapter finishes,
# the next chapter starts only on the next day even if the num of pages read is less than x.
from typing import List


class Solution:
    def f(self, pages, x):
        # 计算x的速度下要多久读完所有书
        hours = 0
        for i in range(len(pages)):
            # 或写成 hour += math.ceil(pile / x)
            hours += pages[i] // x
            if pages[i] % x > 0:
                hours += 1

        return hours

    def findMinimumPagesPerDay(self, pages: List[int], days: int) -> int:
        """
        Time O(n * log(m))
        Space O(1)
        同875，如果遇到一个算法问题，能够确定 x, f(x), target 分别是什么，并写出单调函数 f 的代码，那么就可以运用二分搜索的思路求解。
        一模一样的思路，只是换一个参数名字。
        """
        # 构建边界
        left = 1
        # 这里最大边界是我们一天能读完书的上线也就是max
        right = max(pages)

        # 标准找左边界写法
        while left <= right:
            mid = left + (right - left) // 2
            hours = self.f(pages, mid)
            # 因为这里是单调递减函数，所以小于等于目标值的时候，我们要移动的是右指针
            if hours < days:
                right = mid - 1
            elif hours == days:
                right = mid - 1
            # 大于目标值移动左指针
            else:
                left = mid + 1

        return -1 if left > max(pages) else left


s = Solution()
print(s.findMinimumPagesPerDay(pages=[5, 3, 4], days=4))
print(s.findMinimumPagesPerDay(pages=[2, 3, 4, 5], days=5))
print(s.findMinimumPagesPerDay(pages=[2, 3, 4], days=4))
print(s.findMinimumPagesPerDay(pages=[5, 3, 1, 5, 3, 2, ], days=2))
