from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        """
        Time O(n^2)
        Space O(n)
        dp[i] 定义以i结尾的书架最多可能拿多少本书
        动态规划思路，每次遇到小于前面的书的时候，我们两种选择，第一种前面的不要，从新开始，第二种，前面的一次递减1，累加到当前书架。取最大值。
        但是超时，worse case 所有书架都是单调递减，则遍历每一个书架的时候都需要每次向前倒序遍历一次更新一次递减的情况。
        """
        # 初始化dp数组
        dp = [0] * len(books)
        dp[0] = books[0]
        # 初始化结果，需要一直更新，可能在中间情况的时候达到最大值
        res = dp[0]
        # 遍历书架
        for i in range(1, len(books)):
            # 如果当前的书架大于之前的，则直接拿所有的可以
            if books[i] > books[i - 1]:
                dp[i] = dp[i - 1] + books[i]
            # 反之我们需要更新之前的书架拿的书
            else:
                # 记录当前结果
                start = books[i]
                tmp = books[i]
                # 反向遍历，逐步递减1
                for j in range(i - 1, -1, -1):
                    # 如果已经达到0，说明我们不再需要继续拿了，结束循环
                    if start == 0:
                        break
                    # 如果递减可以拿到的书的个数小于书架拥有的个数，则说明可以拿到递减情况下的书
                    if start - 1 < books[j]:
                        start -= 1
                        tmp += start
                    # 如果当前拥有的小于递减的，说明我们直接可以拿dp[j]的结果，并结束遍历
                    else:
                        tmp += dp[j]
                        break
                # 两种情况下的最大值
                dp[i] = max(tmp, books[i])
            # 更新全局最大
            res = max(res, dp[i])

        return res


class Solution2:
    def calculate_sum(self, books, l, r):
        # Helper function to calculate the sum of books in a given range [l, r]
        # cnt不能超过 r - l + 1，在一个单点递减1的区间
        # 同时cnt不能为负数，所以如果r - l + 1 对应的最后一个元素小于0，则说明最多我们递减books[r]个
        cnt = min(books[r], r - l + 1)
        # first = books[r], last = books[r] - cnt + 1
        return (2 * books[r] - (cnt - 1)) * cnt // 2

    def maximumBooks(self, books: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        整个dp的逻辑是一样的，区别在于如果高效的找到index j对应此时的书架的书小于，此时从当前书架递减下来的值。
        及books[j] < books[i] − (i − j)。这样我们就可以在[j, i]区间直接使用高斯数列计算和，再加上dp[j]就可以算出来当前i角标下最大可以
        拿到书的个数。单调递增栈来记录此j的出现，栈顶元素永远是离当前元素i最近的那个断点。
        此题非常非常巧妙的记录了断点j，并且利用数学方式，降低了第一种解法里面的反向loop叠加计算区间和。
        """
        n = len(books)

        stack = []
        dp = [0] * n

        for i in range(n):
            # While we cannot push i, we pop from the stack
            # 当当前书架一次递减到栈顶的j的时候小于栈顶的书架对应的书的个数，说明我们需要计算高斯数列，并且此栈顶元素弹出
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            # Compute dp[i]，计算高斯数列
            if not stack:
                dp[i] = self.calculate_sum(books, 0, i)
            # 如果栈顶元素存在，说明我们找到一个断点j + 区间[j + 1, i]可以计算高斯数列
            else:
                # 断点 j
                j = stack[-1]
                # 计算当前 i 对应的最大值
                dp[i] = dp[j] + self.calculate_sum(books, j + 1, i)

            # Push the current index onto the stack
            stack.append(i)

        # Return the maximum element in the dp array
        return max(dp)


s = Solution2()
print(s.maximumBooks(books=[8, 5, 2, 7, 9]))
print(s.maximumBooks(books=[7, 0, 3, 4, 5]))
print(s.maximumBooks(books=[8, 2, 3, 7, 3, 4, 0, 1, 4, 3]))
print(s.maximumBooks(books=[0, 5, 5, 5]))
print(s.maximumBooks(books=[0, 3, 1, 5, 4]))
