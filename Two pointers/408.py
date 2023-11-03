class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Time O(n)
        two pointers, keep two pointers loop, once find digit find all digit and record sum and str
        (check if it's start with 0), then let word jump by sum, keep check alpha if it's same,
        final check is two pointers both reach the end. 
        """
        i = 0
        j = 0
        num = 0
        s = ''

        while i < len(word) and j < len(abbr):
            while j < len(abbr) and abbr[j].isdigit():
                num = 10 * num + int(abbr[j])
                s += abbr[j]
                j += 1

            if len(s) > 0 and s[0] == str(0):
                return False
            else:
                i += num
                num = 0
                s = ''
            if j < len(abbr) and i < len(word) and abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return True if i == len(word) and j == len(abbr) else False


class Solution2:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Time O(n)
        Space O(1)
        双指针，两个指针同时走，遇到字符判断是否相等，遇到数字，abbr指针往前走走到一直不是数字为止，
        然后判断word指针对应的长度是否在有效范围内，及不能越界，之后word指针跳对应数字的长度，之后继续loop。
        最后判断两个指针是否都走到了最后index，如果是则说明是合理的简写。
        """
        p1 = 0
        p2 = 0
        # 两个指针都在范围内才可以进loop，因为有可能abbr走完了，但是word并没有，此时要出loop，判断为false
        while p1 < len(abbr) and p2 < len(word):
            # 当前abbr字符串
            c = abbr[p1]
            # 如果是字符
            if c.isalpha():
                # 判断是否和word相等
                if c != word[p2]:
                    return False
                # 如果相等同时跳到下一个index
                p1 += 1
                p2 += 1
            # 如果是数字
            else:
                # 不能是 0 开头
                if int(c) == 0:
                    return False
                # 截取出数字的部分
                start = p1
                # abbr指针向前走直到不是数字
                while p1 < len(abbr) and abbr[p1].isalpha() is False:
                    p1 += 1
                # 提取出数字
                num = int(abbr[start: p1])
                # 判断是否是连续的数字，如果是说明word指针会越界，则为false
                if p2 + num > len(word):
                    return False
                # 如果不是说明是合理的简写，word指针向前跳数字的长度
                else:
                    p2 += num

        # 最后判断是否都同时走到底
        return p2 == len(word) and p1 == len(abbr)


s = Solution2()
print(s.validWordAbbreviation(word="internationalization", abbr="i12iz4n"))
print(s.validWordAbbreviation(word="internationalization", abbr="i5a11o1"))
print(s.validWordAbbreviation(word="hi", abbr="2i"))
