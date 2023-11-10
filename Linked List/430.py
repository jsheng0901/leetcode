# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution1:
    def dfs(self, cur, pre):
        # 如果当前节点是空节点，则返回前一个节点
        if cur is None:
            return pre

        # 当前节点和前一个节点双向链接
        cur.prev = pre
        pre.next = cur

        # 当前节点的下一个节点，暂时存储下来
        tmp = cur.next
        # 找到当前节点child节点的tail，如果没有child，返回当前节点自己
        tail = self.dfs(cur.child, cur)
        # 清空当前节点的child节点
        cur.child = None
        # 继续遍历下一个节点
        return self.dfs(tmp, tail)

    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        """
        Time O(n)
        Space O(n)
        对于双向linked链表，想象成其实就是树，没有child的就是空节点。我们的任务就是遍历树，
        遇到下一层的child节点的时候通过返回值返回下一层的tail来赋值。
        """
        if head is None:
            return head

        # 构建虚拟头结点，方便后面返回原始头结点
        dummy_head = Node(0)
        dummy_head.next = head
        head.prev = dummy_head

        self.dfs(head, dummy_head)
        # 清空头结点的pre指针
        dummy_head.next.prev = None

        return dummy_head.next


class Solution2:
    def dfs(self, cur, pre, tmp):
        # 如果当前节点没有下一个节点没并且没有child节点，说明走到当前level的tail
        if cur.next is None and cur.child is None:
            # 如果有临时节点，则链接当前和上一个临时节点，同时临时节点出栈
            if tmp:
                cur.next = tmp.pop()
            # 如果栈为空，说明走到第一层的tail了，直接赋值prev指针后结束遍历
            else:
                cur.prev = pre
                return

        # 如果有child，判断一下空节点不入栈，非空入栈
        if cur.child:
            if cur.next is not None:
                tmp.append(cur.next)
            # 当前节点下一个节点为child节点
            cur.next = cur.child
            # 清空child节点
            cur.child = None
        # 当前节点前一个节点赋值
        cur.prev = pre
        # 继续遍历下一个节点
        self.dfs(cur.next, cur, tmp)

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time O(n)
        Space O(n)
        同样的思路，区别在于上面通过返回值来赋值，这里类似树前序遍历的全局思路，我们走完所有path，然后用指针来赋值，
        同时用一个栈来存储临时节点，栈头代表需要child节点连接过来的临时节点。多一个栈的思路，space开销大一些。
        """
        if head is None:
            return head

        dummy_head = Node(0)
        dummy_head.next = head

        self.dfs(head, None, [])

        return dummy_head.next

