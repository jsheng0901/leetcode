from collections import defaultdict


class Solution1:
    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        email_to_name = {}
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                email_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
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


s = Solution2()
print(s.accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                                ["John", "johnnybravo@mail.com"]]))
