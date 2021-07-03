def removeExtraSpaces(s):
    """
    use two pointers to remove extra spaces in string s
    与remove一个元素一样，当不满足条件的时候就交换，满足条件时候就让快指针继续走直到找到不满足的元素，而此时慢指针不动，一直在满足条件时候的index
    """
    s = list(s)
    slow_index, fast_index = 0, 0
    while len(s) > 0 and fast_index < len(s) and s[fast_index] == " ":
        fast_index += 1

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


def reverseString(s: [str]):
    """
    0(n/2) time, 0(1) space, loop half of string, use two pointers
    """
    s = list(s)
    end_index = len(s) - 1
    for i in range(len(s) // 2):
        s[i], s[end_index] = s[end_index], s[i]
        end_index -= 1

    return "".join(s)


def reverseWords(s: str) -> str:
    s = removeExtraSpaces(s)
    s = reverseString(s)
    start_index = 0
    result = ""
    for i in range(len(s)):
        if s[i] == " ":
            end_index = i
            result += reverseString(s[start_index:end_index])
            result += ' '
            start_index = end_index + 1
        elif i == len(s) - 1:
            end_index = len(s)
            result += reverseString(s[start_index:end_index])

    return result


print(reverseWords('  a good   example this  '))