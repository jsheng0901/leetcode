# KMP 算法 主要是实现字符串匹配

#  第一步实现 next 数组，目的是记录前缀表最长相等前后缀, 这个理解很重要，什么是前缀，什么是后缀，什么是前缀表和最长相等前后缀
#  此方法为不需要一开始向右集体移动一步，也就是不需要j = -1, next[0] = -1, 都不需要
def get_next(s):
    """
    O(len(s)) time
    """
    next = [0] * len(s)   # 构建next数组placeholder
    j = 0
    for i in range(1, len(s)):  # 注意i从1开始
        while j > 0 and s[i] != s[j]:  # 前后缀不相同了
            j = next[j - 1]  # 向前回溯, 最重要的一步
        if s[i] == s[j]:  # 找到相同的前后缀
            j += 1  # 此时i, j一起向前走一步
        next[i] = j  # 将j（前缀的长度）赋给next[i]

    return next


# 第二步找到next前缀表之后开始loop文本串同时loop模式串，遇到相同就一起+1，不相同就找回上一下不同的前缀表的index
def strStr(haystack: str, needle: str) -> int:
    """
    O(len(haystact + needle)) time
    """
    if len(needle) == 0:
        return 0

    next = get_next(needle)
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = next[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):          # here have to make sure is equal to length since if last is equal j will add one
            return i - len(needle) + 1

    return -1


print(strStr(haystack="hello", needle="ll"))
