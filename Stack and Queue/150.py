def evalRPN(tokens: [str]) -> int:
    """
    O(n) time, 逆波兰表达式：是一种后缀表达式，所谓后缀就是指算符写在后面。
    遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
    """
    stack = []
    for i in tokens:
        if i == "+" or i == "-" or i == "*" or i == "/":
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if i == "+":
                stack.append(num2 + num1)
            elif i == "-":
                stack.append(num2 - num1)
            elif i == "*":
                stack.append(num2 * num1)
            elif i == "/":
                # 这里要注意，如果两个整数除之后是负数，则变成0，反之取商
                stack.append(num2 / num1)
        else:
            stack.append(int(i))

    return int(stack[-1])


print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
