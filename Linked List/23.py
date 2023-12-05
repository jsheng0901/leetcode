from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def merge_two_lists(self, l1, l2):
        # 合并两个链表的模版
        prev_node = ListNode(0)
        prev = prev_node

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        if l1 is None:
            prev.next = l2
        if l2 is None:
            prev.next = l1

        return prev_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time O(k * n)  k number of link list
        Space O(1)
        两两合并，然后loop整个所有list。比较慢虽然可以过所有测试。因为每次合并形成新的链表后需要从新遍历新的链表。
        """
        # 特殊情况
        if len(lists) == 0:
            return None

        if len(lists) == 1 and lists[0] is None:
            return None

        if len(lists) == 1:
            return lists[0]
        # 合并前两个
        new_head = self.merge_two_lists(lists[0], lists[1])
        # 对后续的链表进行合并
        for i in range(2, len(lists)):
            new_head = self.merge_two_lists(new_head, lists[i])
        # 返回新的头结点
        return new_head


class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Time O(n * log(k))  k number of link list
        Space O(k)
        对比第一种写法，用优先列队来存储最小节点值，这样我们每次都可以拿到所有列表中的最小值，和方法1的原理是一样的，
        我们每次拿到的都是当前所有链表中的最小值，并和前一个连起来，但是我们可以缩短这个时间到log(k)利用优先列队。
        同样的我们需要多一个log(k)的存储空间。
        优先队列 pq 中的元素个数最多是 k，所以一次 poll 或者 add 方法的时间复杂度是 O(log(k))，
        所有的链表节点都会被加入和弹出 pq，所以算法整体的时间复杂度是 O(n * log(k))，其中 k 是链表的条数，N 是这些链表的节点总数。
        """
        if not lists:
            return None
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        # 优先级队列，最小堆
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, id(head), head))
        # 将 k 个链表的头结点加入最小堆
        while pq:
            # 获取最小节点，接到结果链表中
            node = heapq.heappop(pq)[2]
            p.next = node
            # 加入新的下一个节点入列队
            if node.next:
                heapq.heappush(pq, (node.next.val, id(node.next), node.next))
            # p 指针不断前进
            p = p.next
        return dummy.next


class Solution3:
    def merge_two_lists(self, l1, l2):
        # 合并两个链表的模版
        prev_node = ListNode(0)
        prev = prev_node

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        if l1 is None:
            prev.next = l2
        if l2 is None:
            prev.next = l1

        return prev_node.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Time ( k * log(n))
        Space O(1)
        分治的思路，先两个merge，0-1，2-3，4-5 --> 0-2，4 --> 0-4。
        总共log(k)次merge，每次n个节点。这里我们可以用in-place memory，所以空间降为常数。
        """
        amount = len(lists)
        interval = 1
        # 分治遍历
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge_two_lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n1.next = n2
n2.next = n3
n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)
n4.next = n5
n5.next = n6
n7 = ListNode(2)
n8 = ListNode(6)
n7.next = n8
s = Solution2()
print(s.mergeKLists(lists=[n1, n4, n7]))
