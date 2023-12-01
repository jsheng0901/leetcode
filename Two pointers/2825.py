class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        Time O(n)
        Space O(1)
        双指针写法，同时遍历两个string，如果相等说明可以组成子序列，则跳过同时进入下一个字符判断，如果不相等看看能不能滚动字符一步之后相等，
        如果可以说明两个指针可以同时前进一步，如果不行，则string1向前走去找下一个可以实现相等的字符，最终判断string2是不是走到底。
        """
        p1 = 0
        p2 = 0

        while p1 < len(str1) and p2 < len(str2):
            s1 = str1[p1]
            s2 = str2[p2]
            # 两个字符相等，走向前走一步
            if s1 == s2:
                p1 += 1
                p2 += 1
            else:
                # 不相等字符，但是滚动字符一步之后相等，两个指针也可以都向前走一步
                if (ord(s1) - 97 + 1) % 26 == ord(s2) - 97:
                    p1 += 1
                    p2 += 1
                # 不相等字符，且滚动字符一步之后也不相等，string1指针向前走
                else:
                    p1 += 1

        # 判断是否string2走到底，也就是string2可以是string1的子序列
        return p2 == len(str2)


s = Solution()
print(s.canMakeSubsequence(str1="abc", str2="ad"))
print(s.canMakeSubsequence(str1="zc", str2="ad"))
print(s.canMakeSubsequence(str1="ab", str2="d"))
