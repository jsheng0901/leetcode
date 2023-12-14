from collections import defaultdict
from typing import List


class Solution:
    def build_graph(self, recipes, ingredients):
        # 初始化记录节点的关系，ingredient -> recipe
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                # 同时记录每个recipe的in degree
                in_degree[recipes[i]] += 1

        return graph, in_degree

    def bfs(self, graph, in_degree, recipes_set, supplies_set):
        # 标准拓扑排序模版
        queue = []
        res = []
        # 找到所有in degree为0的节点，为起始节点，同时需要check是否在supplies里面，如果不在说明不能从此节点出发
        for key in graph.keys():
            if key not in in_degree and key in supplies_set:
                queue.append(key)

        while queue:
            # 当前节点
            cur = queue.pop(0)
            # 遍历当前节点可以去的邻居节点
            for nei in graph[cur]:
                # 邻居节点in degree -1
                in_degree[nei] -= 1
                # 当邻居节点 in degree为0的时候说明我们已经找到所有可以到此节点的ingredient
                if in_degree[nei] == 0:
                    # 如果此节点是recipe，接入结果
                    if nei in recipes_set:
                        res.append(nei)
                    # supplies_set.add(nei)
                    # 这里不再需要判断是否在supplies里面，因为可以制作出来的recipe一定可以加入下一个遍历节点
                    queue.append(nei)

        # 返回结果
        return res

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        Time O(v + e)    ingredients + recipes
        Space O(v + e)
        拓扑排序用于解决从degree 0 开始的有向图。这里我们可以同理210题目，ingredient是前置课程，recipe是完成的课程，构建graph，每个节点
        是ingredient + recipe，如果in degree 为0说明我们可以做出此recipe，此时check一下是不是recipe，如果是的话加入结果。
        初始化的时候判断一下所有in degree是0的ingredient是否在supplies里面，如果不在则不能从此节点开始。
        """
        # 初始化graph和in_degree
        graph, in_degree = self.build_graph(recipes, ingredients)
        # 转化成set方便后续check
        recipes_set = set(recipes)
        supplies_set = set(supplies)
        # 拓扑排序BFS遍历整个graph
        res = self.bfs(graph, in_degree, recipes_set, supplies_set)

        return res


s = Solution()
print(s.findAllRecipes(recipes=["bread", "sandwich", "burger"],
                       ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                       supplies=["yeast", "flour", "meat"]))
