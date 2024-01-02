class Solution1:
    def valid_palindromen(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def maxPalindromes(self, s: str, k: int) -> int:
        """
        Time O(n^2)
        Space O(n)
        两层循环找状态转移，如果当前切割是回文，则等于当前切割点的状态 + 当前切割出来的这个回文。
        但是超时，因为当s特别长的时候k特别小的时候最后一个切割点需要遍历前面几乎所有切割点的状态，非常费时，思路2改进了此处遍历的次数，
        我们并不需要遍历所有之前的切割点，只需要遍历长度是 k和k + 1这两个切割点。详细见下面注释。
        """
        dp = [0] * (len(s) + 1)

        for i in range(1, len(s) + 1):
            # 遍历此切割点前面所有切割点
            for j in range(i):
                # 小于要求长度直接赋值之前切割点状态
                if i - j < k:
                    dp[i] = max(dp[i], dp[j])
                # 反之check是否有回文，然后取最大值
                else:
                    sub_s = s[j: i]
                    if self.valid_palindromen(sub_s):
                        dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]


class Solution2:
    def valid_palindromen(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def maxPalindromes(self, s: str, k: int) -> int:
        """
        Time O(n * K)
        Space O(n)
        整体思路同第一个，当这里有个非常巧妙的思路，当我们的回文长度大于等于 k + 2的时候，我们可以只check移除头尾的情况下的回文是否是回文，
        因为如果是则大于的情况一定是，比如下面里面第二个中间 'cabac' 我们只需要check ’aba‘ + ’c’ + ‘aba‘ 的情况当index到最后一个a的时候，
        并不需要check 'aba' + 'cabac'，这时候我们大大降低了内层循环从 n^2 -> n * k。这里为什么要check k和k+1是因为有奇数和偶数回文两种
        情况比如例子2我们是check ’cabac‘ 的奇数长度 k 'aba'，而例子三我们是check ’cabbac‘ 的偶数长度 k + 1 'abba'，此时只check奇数
        的话我们会漏掉 ’cabbac‘ 此回文的情况。
        """
        # 构建dp数组，初始化为0
        dp = [0] * (len(s) + 1)

        # 从k开始遍历，小于k都不可能
        for i in range(k, len(s) + 1):
            # 如果后续的切割回文都不符合回文，当前dp状态同前一步状态
            dp[i] = dp[i - 1]
            # 遍历奇数偶数两种情况
            for length in range(k, k + 2):
                j = i - length
                # 如果为负数，直接break，当下一个切割点
                if j < 0:
                    break
                # 子序列
                sub_s = s[j: i]
                # check是不是回文
                if self.valid_palindromen(sub_s):
                    # 如果是当前状态等于取当前状态或者前一步是回文的值，加上此时这个回文个数 1
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]


s = Solution2()
print(s.maxPalindromes(s="abacabacdbbd", k=2))
print(s.maxPalindromes(s="abacabacdbbd", k=3))
print(s.maxPalindromes(s="abacabbacdbbd", k=3))
