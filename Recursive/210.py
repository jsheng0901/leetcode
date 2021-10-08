from collections import defaultdict


class Solution:
    """O(v+e) time, v is number of vertex, e is number of edge, O(v+e) space same as time"""
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)
        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        order = []
        is_possible = True
        # white as no pass, gray as pass, black as finish to end node
        color = {k: 'white' for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible

            if not is_possible:
                return

            color[node] = 'gray'
            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == 'white':
                        dfs(neighbor)
                    elif color[neighbor] == 'gray':
                        # An edge to a GRAY vertex represents a cycle
                        is_possible = False
            # Recursion ends. We mark it as black
            # we store last finish course into stack first, like post order
            color[node] = 'black'
            order.append(node)

        for vertex in range(numCourses):
            if color[vertex] == 'white':
                dfs(vertex)

        return order[::-1] if is_possible else []

