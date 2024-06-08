from typing import List


class Solution:
    def __init__(self):
        self.max_length = float('-inf')

    def is_unique(self, subsequence):

        # 用set来判断是否有重复的字符
        visited = set()
        for s in subsequence:
            # 如果有重复的直接返回false
            if s in visited:
                return False
            # 没有重复的，加入set
            else:
                visited.add(s)

        return True

    def backtracking(self, arr, start_index, path):
        # 走到底了，直接结束递归
        if start_index == len(arr):
            return

        # 回溯所有可能的选择
        for i in range(start_index, len(arr)):
            # 加入path
            path.append(arr[i])
            # 当前subsequence
            subsequence = "".join(path)
            # 如果符合条件都是unique的，继续回溯
            if self.is_unique(subsequence):
                # 更新最长长度
                self.max_length = max(self.max_length, len(subsequence))
                # 递归
                self.backtracking(arr, i + 1, path)
            # 回溯弹出当前节点
            path.pop()

        return

    def maxLength(self, arr: List[str]) -> int:
        """
        Time O(2^n)
        Space O(n)
        直接回溯找到所有subsequence的组合，然后判断是否组合里面含有重复的character，如果有则不再递归下去，如果没有更新最长长度，继续添加
        subsequence。注意有可能最终答案不存在这个的subsequence，则返回0。
        """
        # 记录走过的subsequence
        path = []
        self.backtracking(arr, 0, path)

        return 0 if self.max_length == float('-inf') else self.max_length


class Solution2:
    def dfs(self, arr, start_index, res):
        # 如果不符合要求，直接返回0
        if len(res) != len(set(res)):
            return 0

        # 当前节点最短长度
        sub = len(res)
        for i in range(start_index, len(arr)):
            # 子节点返回值的长度
            tmp = self.dfs(arr, i + 1, res + arr[i])
            # 找到最大返回长度
            sub = max(sub, tmp)

        # 返回结果
        return sub

    def maxLength(self, arr: List[str]) -> int:
        """
        Time O(2^n)
        Space O(n)
        DFS递归后续遍历的的思路，每次我们判断当前节点的path是否有重复的character，如果有直接返回0，没有继续递归，
        当前节点返回值最小也是当前path的长度，加上后序遍历返回来的结果，返回最长长度。
        """
        return self.dfs(arr, 0, "")


s1 = Solution()
print(s1.maxLength(arr=["un", "iq", "ue"]))
s2 = Solution()
print(s2.maxLength(arr=["cha", "r", "act", "ers"]))
s3 = Solution()
print(s3.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))
s4 = Solution()
print(s4.maxLength(arr=["aa", "bb"]))
