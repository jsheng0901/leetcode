class Solution:
    def is_cycle(self, curr, courseDict, checked, path):
        if checked[curr]:
            return False

        if path[curr]:
            return True

        path[curr] = True

        result = False
        if curr in courseDict:
            for child in courseDict[curr]:
                result = self.is_cycle(child, courseDict, checked, path)
                if result:
                    break

        path[curr] = False
        checked[curr] = True

        return result

    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        """DFS back tracking的方式，搜索是否有循环，同时记录每次走过的节点是否是true，并记录这个节点是否被check过"""
        courseDict = {}

        for p in prerequisites:
            nextCourse, prevCourse = p[0], p[1]
            if prevCourse not in courseDict:
                courseDict[prevCourse] = [nextCourse]
            else:
                courseDict[prevCourse].append(nextCourse)

        checked = [False] * numCourses
        path = [False] * numCourses

        for curr in range(numCourses):
            if self.is_cycle(curr, courseDict, checked, path):
                return False

        return True

s = Solution()
print(s.canFinish(2, [[1,0]]))
