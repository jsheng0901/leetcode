from collections import defaultdict
from typing import List


class Solution1:
    def dfs(self, curr, course_dict, checked, path):
        # if check before than no cycle return False
        if checked[curr]:
            return False
        # if cur node shows again in DFS path, means there is cycle, then return True
        if path[curr]:
            return True
        # mark the current node as visited and part of current recursion path.
        path[curr] = True
        checked[curr] = True

        result = False
        if curr in course_dict:
            for child in course_dict[curr]:
                result = self.dfs(child, course_dict, checked, path)
                if result:
                    break
        # Remove the node from the path, after finish this DFS check
        path[curr] = False

        return result

    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        """
        n be the number of courses and m be the size of prerequisites
        Time O(m + n) 初始化dict用O(m)，dfs走遍所有course用O(n)v
        Space O(m + n) 初始化dict用O(m)，dfs走遍所有course用O(n)，初始化visited和check用O(n)
        DFS back tracking的方式，搜索是否有循环，同时记录每次走过的节点是否是true，并记录这个节点是否被check过
        """
        # 用dict的方式记录每个课程之间的关系
        course_dict = {}

        for p in prerequisites:
            next_course, prev_course = p[0], p[1]
            if prev_course not in course_dict:
                course_dict[prev_course] = [next_course]
            else:
                course_dict[prev_course].append(next_course)

        checked = [False] * numCourses
        path = [False] * numCourses

        for curr in range(numCourses):
            if self.dfs(curr, course_dict, checked, path):
                return False

        return True


class Solution2:
    def __init__(self):
        self.path = None
        self.visited = None
        self.cycle = False

    def dfs(self, course_dict, course):
        # 出现环
        if self.path[course]:
            self.cycle = True
            return

        # 如果已经找到了环，也不用再遍历了
        if self.cycle or self.visited[course]:
            return

        # 前序遍历代码位置，此时达到当前节点，处理当前节点逻辑。
        self.visited[course] = True
        self.path[course] = True

        for nei in course_dict[course]:
            self.dfs(course_dict, nei)

        # 后序遍历代码位置，此时离开当前节点，体现回溯逻辑，回到上一个节点。
        self.path[course] = False

        return

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time O(m + n) 初始化dict用O(m)，dfs走遍所有course用O(n)v
        Space O(m + n) 初始化dict用O(m)，dfs走遍所有course用O(n)，初始化visited和check用O(n)
        逻辑同上，区别在于，设计全局参数cycle记录是否有环出现，不需要通过dfs返回值来判断最终结果。区别就是遍历整个图用返回值来判断逻辑，
        还是遍历整个图用找到符合条件的路径来判断逻辑。
        """
        course_dict = defaultdict(list)
        for p in prerequisites:
            next_course, prev_course = p[0], p[1]
            course_dict[prev_course].append(next_course)

        self.path = [False] * numCourses
        self.visited = [False] * numCourses

        # 遍历图中的所有节点，这里需要手动加loop因为可能有完全不相链接的graph
        for course in range(numCourses):
            self.dfs(course_dict, course)

        return self.cycle is False


s = Solution2()
print(s.canFinish(2, [[1, 0]]))
