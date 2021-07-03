def removeExtraSpaces(s):
    """
    use two pointers to remove extra spaces in string s
    """
    s = list(s)
    slow_index, fast_index = 0, 0
    # 移除开始的空白
    while len(s) > 0 and fast_index < len(s) and s[fast_index] == " ":
        fast_index += 1

    # 移除s中间的多余空格
    for fast_index in range(fast_index, len(s)):
        if fast_index - 1 > 0 and s[fast_index] == s[fast_index - 1] and s[fast_index] == " ":
            continue
        else:
            s[slow_index] = s[fast_index]
            slow_index += 1

    if slow_index - 1 > 0 and s[slow_index - 1] == " ":         # 移除结尾多余的空格
        return "".join(s[:slow_index - 1])
    else:
        return "".join(s[:slow_index])


def reverseString(s):
    """
    0(n/2) time, 0(1) space, loop half of string, use two pointers
    """
    s = list(s)
    j = len(s) - 1    # left pointer
    for i in range(len(s) // 2):     # loop only half string
        s[i], s[j] = s[j], s[i]                  # change position
        j -= 1

    return "".join(s)


def reverseWords(s: str) -> str:
    """
    O(n) time, O(1) space, 整体思路：先移除所有多余空格，在反转整个string，在逐一反转每个单词
    """
    s = removeExtraSpaces(s)
    s = reverseString(s)
    start = 0
    result = ''
    for i in range(len(s)):
        if s[i] == ' ':
            end = i
            result += reverseString(s[start:end])
            result += ' '
            start = end + 1
        elif i == len(s) - 1:
            end = len(s)
            result += reverseString(s[start:end])

    return result


print(reverseWords('a good   example'))
