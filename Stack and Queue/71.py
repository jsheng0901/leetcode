class Solution1:
    def simplifyPath(self, path: str) -> str:
        """
        Time O(n)
        Space O(n)
        loop一次，找到两个/之间的字符串的时候进行判断，没有遇到下一个/之前一直累加字符并判断.和字母的个数
        """
        stack = []
        dot_number = 0
        ch_number = 0
        i = 0
        name = ''
        res = '/'

        while i < len(path):
            if path[i] == '/':
                i += 1

            while i < len(path) and path[i] != '/':  # 找到所有两个/之间的字符串
                name += path[i]
                if path[i] == '.':
                    dot_number += 1
                elif path[i].isalpha():
                    ch_number += 1
                i += 1

            # 判断三种情况: 1: 只有. 2: .和字母 3: 只有字母

            if dot_number > 0 and ch_number == 0:  # 只有.
                if dot_number == 2:
                    if len(stack) > 0:
                        stack.pop()
                elif dot_number > 2:
                    stack.append('.' * dot_number)
                dot_number = 0
            elif ch_number > 0:  # 剩下两种情况
                stack.append(name)
            # 注意回归default状态, 找下一个两个/之间的字符串
            name = ''
            ch_number = 0
            dot_number = 0

        res += "/".join(stack)
        return res


class Solution2:
    def simplifyPath(self, path: str) -> str:
        """
        Time O(n)
        Space O(n)
        直接用build in split function，遇到一个点或者没有东西就跳过，遇到两个点就弹出，其它情况加入stack
        """
        # Initialize a stack
        stack = []

        # Split the input string on "/" as the delimiter
        # and process each portion one by one
        for portion in path.split("/"):

            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stitch together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str


class Solution3:
    def simplifyPath(self, path: str) -> str:
        """
        Time O(n)
        Space O(n)
        同思路2，但是最后累加方式不一样。
        """

        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(part)

        res = ""
        while stack:
            res = "/" + stack.pop() + res

        return res if res else "/"


s = Solution3()
print(s.simplifyPath(path='/home/'))
print(s.simplifyPath(path="/home//foo/"))
