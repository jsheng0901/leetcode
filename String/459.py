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
            j = next[j - 1]  # 向前回溯
        if s[i] == s[j]:  # 找到相同的前后缀
            j += 1  # 此时i, j一起向前走一步
        next[i] = j  # 将j（前缀的长度）赋给next[i]

    return next


def repeatedSubstringPattern(s: str) -> bool:
    """
    O(n) time, find repeat 部分, 这里只要用KMP找到next数组就行，难度在理解如何验证是否存在，next数组最后一个数及是最长前后缀+1
    """
    if len(s) == 0:
        return False

    next = get_next(s)
    l_str = len(s)
    if next[l_str - 1] != 0 and l_str % (l_str - (next[l_str - 1])) == 0:
        return True
    else:
        return False


print(repeatedSubstringPattern("abcabcabcc"))