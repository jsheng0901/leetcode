def removeDuplicates(S: str) -> str:
    """
    O(n) time same as 20, if have duplicate then remove, otherwise append to stack
    """
    stack = []
    for i in S:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    # 构建剩下的字符串变成string，不用list.join()       return ''.join(stack)
    result = ''
    while len(stack) > 0:
        result += stack.pop()

    return result[::-1]   # 反转string, 因为stack pop出来的顺序是反的


print(removeDuplicates('abbaca'))

