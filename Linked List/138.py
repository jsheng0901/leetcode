class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1(object):
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def get_cloned_node(self, node):
        # If node exists then
        if node:
            # Check if it's in the visited dictionary
            if node in self.visited:
                # If it's in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        Time O(n)
        Space O(n)
        遍历整个linked list，存储原来的linked list 作为 key，new linked list 作为 value，如果我们遇到遍历过的就直接返回新的node，
        如果没有遍历过的，就构建新的node，同时赋予节点next和random指针。
        """

        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node is not None:
            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.get_cloned_node(old_node.random)
            new_node.next = self.get_cloned_node(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]


class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Time O(n)
        Space O(n)
        分步骤写两次遍历，第一次存储新的节点和老节点的关系，第二次连接上所有关系。
        对于数据结构复制，甭管他怎么变，最简单的方式：一个哈希表 + 两次遍历。
        第一次遍历专门克隆节点，借助哈希表把原始节点和克隆节点的映射存储起来；第二次专门组装节点，照着原数据结构的样子，把克隆节点的指针组装起来。
        如果克隆带随机指针的二叉树，或者克隆图，都是一样的，只不过是遍历的方式从 for 循环迭代遍历变成 traverse 递归函数遍历罢了。
        """
        originToClone = {}
        # 第一次遍历，先把所有节点克隆出来
        p = head
        while p:
            if p not in originToClone:
                originToClone[p] = Node(p.val)
            p = p.next
        # 第二次遍历，把克隆节点的结构连接好
        p = head
        while p:
            if p.next:
                originToClone[p].next = originToClone[p.next]
            if p.random:
                originToClone[p].random = originToClone[p.random]
            p = p.next
        # 返回克隆之后的头结点
        return originToClone.get(head)


class Solution3:
    def __init__(self):
        self.originToClone = None
        self.visited = None

    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Time O(n)
        Space O(n)
        分步骤写两次遍历，第一次存储新的节点和老节点的关系，第二次连接上所有关系。
        用递归的方式进行遍历
        """
        self.visited = set()
        self.originToClone = {}
        self.traverse(head)
        return self.originToClone.get(head)

    # DFS 图遍历框架
    def traverse(self, node):
        if not node:
            return
        if node in self.visited:
            return
        # 前序位置，标记为已访问
        self.visited.add(node)
        # 前序位置，克隆节点
        if node not in self.originToClone:
            self.originToClone[node] = Node(node.val)
        cloneNode = self.originToClone[node]

        # 递归遍历邻居节点，并构建克隆图
        # 递归之后，邻居节点一定存在 originToClone 中
        self.traverse(node.next)
        cloneNode.next = self.originToClone.get(node.next)

        self.traverse(node.random)
        cloneNode.random = self.originToClone.get(node.random)


class Solution4(object):
    def copyRandomList(self, head):
        """
        Time O(n)
        Space O(1)
        此方法不需要额外的dictionary空间来存储visited过的node，在原来的基础上直接构建新的node，并从新构建random后在拆开原来的
        node和新的node
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:
            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Un-weave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head  # A->B->C
        ptr_new_list = head.next  # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new


l1 = Node(1)
l2 = Node(2)
l1.next = l2
l1.random = l2
l2.random = l2

s = Solution2()
print(s.copyRandomList(l1))
