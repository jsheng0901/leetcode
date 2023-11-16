from typing import List


class Solution:
    def valid(self, s, start, forbidden_set):
        # 回溯切割，后续遍历判断返回值，在节点处理解释的时候
        if start == len(s):
            return True
        # 收集所有子节点的返回值
        res = []
        for i in range(start, len(s)):
            # 当前切割子串
            sub = s[start: i + 1]
            # 如果在forbidden里面直接返回 false
            if sub in forbidden_set:
                return False
            # 如果不在，继续递归
            sub_res = self.valid(s, i + 1, forbidden_set)
            res.append(sub_res)
        # 必须所有子节点都是 true 才是合理的切割
        return all(res)

    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        """
        Time O(n * n^2)
        Space O(n)
        双指针左右移动窗口找substring，每次右一定一个位置，判断窗口内的substring是不是合理的，用回溯的方式切割所有可能性并判断，
        如果不合理则左指针向前走缩减窗口，并同时判断是否合理，左指针停止走直到找到合理的窗口。之后继续右指针，
        此方法在回溯的过程中有很多重复的切割，因为这个是substring是连续的子串，所以我们可以用到之前check过的信息。
        这里应用了memo来存储查存过的窗口，不过还是超时，回溯不可避免的有重复切割判断，详细例子见解法2。
        """
        left, right = 0, 0
        max_substring = 0
        forbidden_set = set(forbidden)
        window = ""
        memo = {}
        while right < len(word):
            # c 是将移入窗口的字符
            c = word[right]
            # 扩大窗口
            right += 1
            # 进行窗口内数据的一系列更新
            window += c
            # check窗口是否合理
            is_valid = self.valid(window, 0, forbidden_set)

            # 如果不合理，移动左指针直到合理
            while is_valid is False:
                # 记录不合理的窗口进备忘录
                memo[window] = False
                # 缩小窗口
                left += 1
                # 左指针缩小窗口
                window = window[1:]
                is_valid = self.valid(window, 0, forbidden_set)

            # 记录合理的窗口进备忘录
            memo[window] = True
            # 更新最大值
            max_substring = max(max_substring, len(window))

        return max_substring


class Solution2:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        """
        Time O(n^2)
        Space O(n)
        双指针写法，此题特别独特的地方在于，当加入新的字符后，我们只需要让左指针到新的右指针的范文内loop一遍所有的substring，
        同时判断是否在forbidden里面，如果在，说明新加入的导致新的substring不合规，则更新左指针到违规index的下一个。
        例子：'baa' 是合理的substring，加入 'a' 之后 -> 'baaa'，此时我们并不需要重新切分所有可能去判断 'baaa' 是不是合理的，
        我们只需要判断 'baaa' 'aaa' 'aa' 'a' 这四个substring即可，并不需要判断 'ba' 'b' 'baa' 之类的substring。
        因为在 'baa' 的时候已经判断过。所以第一种用回溯的方式枚举所有切割再判断的方式会产生很多没必要的切割和判断。
        则直接双指针移动左指针即可。
        """
        # 转化成集合方便快速查存在
        forbidden_set = set(forbidden)
        res = 0
        left = 0
        # 右指针遍历
        for i in range(len(word)):
            # j指针遍历左指针到右指针整个区间
            # 这里有个优化是取左指针和右指针-10最大值，因为forbidden最长是10，所以我们维护一个最大为10的窗口即可
            for j in range(max(left, i - 10), i + 1):
                # 如果在forbidden里面，则更新左指针到下一个index
                if word[j:i + 1] in forbidden_set:
                    left = j + 1
            # 更新最长substring
            res = max(res, i - left + 1)

        return res


s = Solution2()
print(s.longestValidSubstring(word="cbaaaabc", forbidden=["aaa", "cb"]))
