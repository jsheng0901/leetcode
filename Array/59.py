def generateMatrix(n: int) -> [[int]]:
    """
    O(n ^ 2) time

    循环永远只走左闭右开区间
    """
    matrix = [[None for i in range(n)] for i in range(n)]  # defined n * n metrix first
    start_x, start_y = 0, 0   # 定义循环的起始位置
    loop = n // 2    # 定义循环的次数
    mid = n // 2     # 定义中间数的位置
    offset = 1       # 每一圈循环，需要控制每一条边遍历的长度
    count = 1        # 计数
    while loop > 0:
        i, j = start_x, start_y

        for j in range(start_y, start_y + n - offset):
            matrix[i][j] = count
            count += 1

        j += 1         # 当循环走出来的时候 j = n - 2，因为我们设置的是左闭右开区间，因此要手动向前跳到最后一行及 n - 1 index的位置

        for i in range(start_x, start_x + n - offset):
            matrix[i][j] = count
            count += 1

        i += 1        # 同上

        for j in range(j, start_y, -1):    # range 开始的位置是j所在的位置，因为我们之前手动跳到了此处
            matrix[i][j] = count
            count += 1

        j -= 1       # 当循环走出来的时候 j = start_y + 1，因为我们设置的是左闭右开区间，因此要手动向前跳到开始的那行行及 start_y 的位置

        for i in range(i, start_x, -1):    # range 开始的位置是i所在的位置，因为我们之前手动跳到了此处
            matrix[i][j] = count
            count += 1

        i -= 1       # 同上

        start_x += 1       # 下一次loop时候开始位置都要移动一格
        start_y += 1       # 下一次loop时候开始位置都要移动一格
        offset += 2        # 下一次loop时候两边不走的多处两行
        loop -= 1
    if n % 2 > 0:  # 当数字为奇数的时候需要单独设置中间数字
        matrix[mid][mid] = count

    return matrix


print(generateMatrix(5))


