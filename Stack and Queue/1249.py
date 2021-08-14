class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        当遇到不是(时候并且stack为空的时候，就说明遇到了要移除的）符号，这里最巧妙的是记录index而不是符号本身
        多余的（符号会记录在最终的stack里面，这些都是要被移除的符号
        """
        index_to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == '(':
                stack.append(i)
            elif len(stack) == 0:
                index_to_remove.add(i)
            else:
                stack.pop()

        index_to_remove = index_to_remove.union(set(stack))

        result = []
        for i, c in enumerate(s):
            if i not in index_to_remove:
                result.append(c)

        return "".join(result)

