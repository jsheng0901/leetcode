class Solution:
    def dp(self, s, left, right, k, memo):
        # 如果已经没有k了，直接返回false
        if k < 0:
            return False

        # 如果走到底了说明找打了一条path，返回true
        if left >= right:
            return True

        # 遇见之前访问过的状态，直接返回结果
        if memo[left][right][k] != -1:
            return memo[left][right][k]

        # 记录子节点的返回结果，只要有一天valid的path即可
        res = False
        # 左右相等，同时移动指针，k不变
        if s[left] == s[right]:
            res = res or self.dp(s, left + 1, right - 1, k, memo)
        # 左右不相等，两种走法，同时k消耗1
        else:
            res = res or self.dp(s, left + 1, right, k - 1, memo)
            res = res or self.dp(s, left, right - 1, k - 1, memo)

        # 记录当前节点切割的状态结果
        memo[left][right][k] = res

        return res

    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        Time O(n^2 * k)
        Space O(n^2 * k)
        基本的dp带备忘录的写法，每一次遇到不相等的字符，可以左右个选择一种走法，本质上我们是回溯找到所有写个方法然后返回一条可能的path，
        用备忘录记录所有状态，然后同一种状态可以直接返回结果。这里需要遍历三总状态的和，左右节点的位置和当前用了多少k。
        """
        length = len(s)
        # 初始化备忘录
        memo = [[[-1] * (k + 1) for _ in range(length)] for _ in range(length)]

        left = 0
        right = len(s) - 1

        return self.dp(s, left, right, k, memo)


class Solution2:
    def dp(self, s, left, right, memo):
        # 走到底，返回0，没有用k
        if left >= right:
            return 0

        # 走到最后两个字符，需要判断一下是否相等，来确定用没用k
        if left == right - 1:
            return 1 if s[left] != s[right] else 0

        # 遇见之前访问过的状态，直接返回结果
        if memo[left][right] != -1:
            return memo[left][right]

        # 遇到相等的，直接返回结果，并赋值备忘录
        if s[left] == s[right]:
            res = self.dp(s, left + 1, right - 1, memo)
            memo[left][right] = res
        # 遇到不相等的，两个子path的结果去最小值，并赋值备忘录
        else:
            left_node = self.dp(s, left + 1, right, memo)
            right_node = self.dp(s, left, right - 1, memo)

            res = 1 + min(left_node, right_node)
            memo[left][right] = res

        return res

    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        Time O(n^2)
        Space O(n^2)
        同思路1，只是这里我们找到最短的path，然后判断一下最短的path用的k，然后判断一下是否小于等于题目给的k即可，这样会快很多，
        因为我们没必要记录第三个状态k值，大大缩短了遍历的次数和空间使用。
        """
        length = len(s)
        # 同上，初始化备忘录，只是这里是2D
        memo = [[-1] * length for _ in range(length)]

        left = 0
        right = len(s) - 1

        return self.dp(s, left, right, memo) <= k


s = Solution()
print(s.isValidPalindrome(s="abcdeca", k=2))
print(s.isValidPalindrome(s="abbababa", k=1))
print(s.isValidPalindrome(s="bacabaaa", k=2))
