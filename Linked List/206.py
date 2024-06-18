from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:

    # def reverse(self, pre, cur):
    #     if cur is None:
    #         return pre
    #     temp = cur.next
    #     cur.next = pre
    #     # 可以和双指针法的代码进行对比，如下递归的写法，其实就是做了这两步
    #     # pre = cur;
    #     # cur = temp;
    #
    #     return self.reverse(cur, temp)
    #
    # def reverseList_1(self, head: ListNode) -> ListNode:
    #     pre = None  # 初始化过程和two pointer 一样
    #     cur = head
    #
    #     return self.reverse(pre, cur)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time O(n)
        Space O(1)
        双指针写法，loop写法，其实更高效因为不用递归栈。
        """
        current = head  # start from firs head
        previous = None  # previous head node which is None at first
        while current:  # loop over linked node, when next is None then out
            tmp = current.next  # save current next node as temp node because this will be next current node
            current.next = previous  # point link back to previous node
            previous = current  # move previous to current node, this must move firs then current pointer
            current = tmp  # move current to temp node

        return previous  # return new head


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time O(n)
        Space O(n)
        真正递归的写法来实现翻转链表，类似后续遍历的思路，走到最后，然后开始层层翻转。详细见注释。
        """
        # 如果链表为空或者只有一个节点的时候，反转结果就是它自己，直接返回即可。
        if not head or not head.next:
            return head

        # 返回反转之后的新的头节点
        last = self.reverseList(head.next)

        # 当前节点的下一个节点的下一个指针，指向自己，也就是 5 -> 6 变成 6 -> 5，实现翻转
        head.next.next = head

        # 当前节点的下一个指针释放为空，因为已经翻转了下一个节点的指向
        # 并且新的头结点是 last，而当前节点 head 变成了最后一个节点，链表的末尾要指向 null
        head.next = None

        # 反正新的头节点，也就是最后一个头节点，其次递归每一层都是返回一样的节点，也就是原先的最后一个节点，也是新的头节点。
        return last


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
s = Solution2()
reverse_linked_list = s.reverseList(l1)
print(reverse_linked_list.val)
