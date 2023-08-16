from collections import defaultdict


class Solution1:
    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        """
        Time O(NKlogNK) N is number of account, k is max length of account, DFS需要走完所有account及node，sort需要logNK
        Space O(NK) build adjacency list需要NK，seen也需要NK，DFS系统stack也需要NK
        """
        email_to_name = {}
        graph = defaultdict(set)
        # 构建graph，用dictionary的方式，表示first email链接所有其它email和email链接first email，并记录email对名字
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                email_to_name[email] = name

        seen = set()
        ans = []
        # stack way to write dfs
        # for email in graph:
        #     if email not in seen:
        #         seen.add(email)
        #         stack = [email]
        #         component = []
        #         while stack:
        #             node = stack.pop()
        #             component.append(node)
        #             for nei in graph[node]:
        #                 if nei not in seen:
        #                     seen.add(nei)
        #                     stack.append(nei)
        #         ans.append([email_to_name[email]] + sorted(component))

        def dfs(component, email):
            # 记录进入dfs里面的email，能进递归一定先判断过符合条件
            seen.add(email)
            component.append(email)
            for nei in graph[email]:    # loop所有邻居节点并判断是否seen过，没有见过则进入dfs递归
                if nei not in seen:
                    dfs(component, nei)

        # loop循环check每一个node在graph里面
        for email in graph:
            # 如果没有见过则说明是全新的component
            if email not in seen:
                # 初始化这个component为空
                component = []
                dfs(component, email)
                # 走完所有dfs路径后得到这个component所有节点，加入最终answer
                ans.append([email_to_name[email]] + sorted(component))

        return ans


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        """find parent node which corresponding index equal to self ex: index 4 of list == 4"""
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # 找到parent并且赋值给child index, 每个child的父节直接连根节点
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)       # 找到x对应的parent index的值
        y_root = self.find(y)
        # 如果不是同一个parent, 则进行合并parent，把 x的index的值变成y对应的值，此时我们把y node作为了x node的parent node
        # x --> y 树结构中
        if x_root != y_root:
            self.parent[x_root] = y_root


class Solution2:
    def accountsMerge(self, accounts: [[str]]) -> [[str]]:

        n = len(accounts)

        uf = UnionFind(n)

        email_to_index = {}

        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in email_to_index:  # save different email to unique index
                    email_to_index[email] = i
                else:
                    # 存在重复的email出现的时候，我们要把email对应的index进行合并
                    uf.union(i, email_to_index[email])
        # 目前email_to_index会记录所有email的对应的index，但是比如index 1对应的email在UF里面已经合并进index 0
        # 上面的操作会把属于同一个email的index进行全部合并
        # 把所有合并后的账户对应的email放进同一个list里面
        index_to_email = defaultdict(list)
        for email, index in email_to_index.items():
            index_to_email[uf.find(index)].append(email)        # uf.find会找到已经被合并的email的index对应的parent index
            # ex: john00@mail.com对应的index是1在accounts里面，但是在UF里面index 1已经和index 0合并，所以email会进入0这个key
        ans = []
        for index, email in index_to_email.items():
            ans.append([accounts[index][0]] + sorted(email))

        return ans


s = Solution1()
print(s.accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                                ["John", "johnnybravo@mail.com"]]))
