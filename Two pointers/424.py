from collections import defaultdict


class Solution1:
    def valid_substring(self, s, substring_length, k):
        # take a window of length `substring_length` on the given
        # string, and move it from left to right. If this window
        # satisfies the condition of a valid string, then we return true
        window = defaultdict(int)
        max_freq = 0
        left = 0
        right = 0
        # 滑动窗口模板
        while right < len(s):
            # 进窗口的元素
            c = s[right]
            right += 1
            # 更新窗口内频率
            window[c] += 1
            # 需要先判断一下窗口是否大于固定长度，如果先计算长度，会出现超过窗口的元素进来后，没有剔除最左边的元素就开始计算长度，此时会增大
            # 实际窗口的大小
            if right - left > substring_length:
                # 离开窗口的元素
                d = s[left]
                # 更新频率
                window[d] -= 1
                # 移动左指针
                left += 1

            # 再计算当前最大频率，如果满足固定长度减去最大频率小于等于k，说明一定可以通过翻转不是最大频率的那些字母达到一致
            max_freq = max(max_freq, window[c])
            # 如果找到满足的条件，直接返回true，解释滑动窗口
            if substring_length - max_freq <= k:
                return True

        # 反之返回false
        return False

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time O(n * log(n))
        Space O(m --> 26) --> O(1)
        此题有一个核心理论是，当长度为n的substring满足条件的时候，长度为n - 1的substring一定满足条件。所以我们可以用二分法固定长度先，
        转化成对于长度是固定的窗口substring，是否能找到满足条件的窗口。详细看注释。
        参考 https://leetcode.com/problems/longest-repeating-character-replacement/editorial/
        """
        # 二分法起点和终点，因为是长度，所以相对于index都要 +1
        left = 1
        right = len(s)

        # 二分法模板，找左边界写法
        while left <= right:
            mid = left + (right - left) // 2
            # 是否当前substring长度满足条件
            valid_length = self.valid_substring(s, mid, k)

            # 满足则，找更大的右边
            if valid_length:
                left = mid + 1
            # 不满足，找更小的左边
            else:
                right = mid - 1

        return left - 1


class Solution2:
    def max_substring(self, s, letter, k):
        # 滑动窗口模板，窗口内统计当前letter出现的次数
        window = 0
        # 记录最长长度
        max_length = 0
        left = 0
        right = 0

        while right < len(s):
            # 进窗口的character
            c = s[right]
            right += 1
            # 如果是当前固定letter，窗口 +1
            if c == letter:
                window += 1

            # 同样需要先判断一下是否是合理的窗口，如果窗口内剩下的letter个数大于k，那么一定不能翻转合理substring，需要收缩窗口
            while right - left - window > k:
                # 弹出的character
                d = s[left]
                left += 1
                # 如果弹出的是固定letter，窗口 -1
                if d == letter:
                    window -= 1

            # 更新当前合理的窗口最大长度
            max_length = max(max_length, right - left)

        return max_length

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time O(m * n --> 26 * n) --> O(n)
        Space O(m --> 26) --> O(1)
        问题转化成，如果固定一个字母不能翻转，那么最长的substring是多少如果其它的字母可以翻转k次。我们只需要遍历所有unique字母然后找
        到最长的substring即可。每次找最长长度用滑动窗口。
        """
        # 找到所有的unique letter
        distinct_letter = set(s)
        res = 0
        # 遍历所有情况
        for letter in distinct_letter:
            # 拿到当前letter固定下最长的substring
            max_length = self.max_substring(s, letter, k)
            # 更新长度
            res = max(res, max_length)

        return res


class Solution3:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time O(n)
        Space O(m --> 26) --> O(1)
        同样的思路1，这里我们并不需要每次固定了窗口长度后从0开始，对于长度为l的substring，如果合理的话，
        我们完全可以继续探索l + 1的长度substring，并不需要从头开始扩大窗口。所以我们只需要找到合理的substring后继续扩大窗口，遇到不合理的
        窗口我们缩小窗口。用同样的方法 窗口大小 - 最大字母 <= k 频率来判断是否合理。
        """
        window = defaultdict(int)
        max_freq = 0
        left = 0
        right = 0
        res = 0
        # 滑动窗口模板
        while right < len(s):
            # 进窗口的元素
            c = s[right]
            right += 1
            # 更新窗口内频率
            window[c] += 1
            # 计算最大的频率目前窗口内
            max_freq = max(max_freq, window[c])

            # 如果窗口不合理，需要收缩窗口，这里的核心是当遇到不合理的substring的时候，此时因为右指针移动了一位，一定是l + 1，
            # 我们只需要移动一位左指针，这样就可以保证窗口内长度继续是l，而不会变小。我们只对更长的合理的substring感兴趣，所以不需要一直
            # 弹出左指针的字母
            if right - left - max_freq > k:
                # 弹出的字母
                d = s[left]
                left += 1
                # 更新窗口
                window[d] -= 1
            # 此时一定是合理的substring，更新长度
            res = right - left

        return res


s = Solution3()
print(s.characterReplacement(s="AABA", k=0))
print(s.characterReplacement(s="AABABBA", k=1))
