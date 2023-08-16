class Solution:
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


s = Solution()
print(s.canFinish(2, [[1, 0]]))
