class DoubleListNode:
    def __init__(self, val, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre


class BrowserHistory:

    def __init__(self, homepage: str):
        """
        Time O(1)
        Space O(n)
        两个stack，一个记录当前所有history的URL，另一个记录当前之前的所有URL。
        此方法后退前进都是O(n)每一个包含两个栈的操作及应该是O(step * 2)，三种方法中此方法最慢。
        """
        self.stack1 = [homepage]
        self.stack2 = []
        self.stack1_size = 1
        self.stack2_size = 0

    def visit(self, url: str) -> None:
        """
        Time O(1)
        叠加新的URL并记录长度用于后续判断
        """
        self.stack1.append(url)
        self.stack1_size += 1
        self.stack2 = []
        self.stack2_size = 0

    def back(self, steps: int) -> str:
        """
        Time O(n)
        第一个stack栈顶是当前访问的URL，弹出后加入另一个栈，第一个stack的栈顶永远是当前访问界面。
        """
        available_steps = min(steps, self.stack1_size - 1)
        while available_steps > 0:
            top = self.stack1.pop()
            self.stack1_size -= 1
            self.stack2.append(top)
            self.stack2_size += 1
            available_steps -= 1

        return self.stack1[-1]

    def forward(self, steps: int) -> str:
        """
        Time O(n)
        同backward原理，第二个栈的栈顶是最后一个加进来的URL，一直弹出直到走到应该走的step。当前界面再第一个stack。
        """
        available_steps = min(steps, self.stack2_size)
        while available_steps > 0:
            top = self.stack2.pop()
            self.stack2_size -= 1
            self.stack1.append(top)
            self.stack1_size += 1
            available_steps -= 1
        return self.stack1[-1]


class BrowserHistory2:

    def __init__(self, homepage: str):
        """
        Time O(1)
        Space O(n)
        双向链表写法，基本上思路和第一种是一样的，区别在于每次前进后退并不需要两个栈进行操作，只需要移动当前指针。
        此方法理论上和第一种一样但是实际上更快一些在前进后退的时候。
        """
        node = DoubleListNode(homepage)
        self.cur = node

    def visit(self, url: str) -> None:
        """
        Time O(1)
        构建新的URL节点，并链接起来
        """
        node = DoubleListNode(url)
        self.cur.next = node
        node.pre = self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        """
        Time O(n)
        指针往前跳
        """
        while self.cur.pre and steps:
            self.cur = self.cur.pre
            steps -= 1

        return self.cur.val

    def forward(self, steps: int) -> str:
        """
        Time O(n)
        同上
        """
        while self.cur.next and steps:
            self.cur = self.cur.next
            steps -= 1

        return self.cur.val


class BrowserHistory3:

    def __init__(self, homepage: str):
        """
        Time O(1)
        Space O(n)
        动态数组写法，此方法最高效，我们一直维护一个数组，当我们前进后退的时候我们改变的是指针的位置，直接通过指针的index和step进行更新
        当前指针的位置，然后直接提取当前指针对应的URL。
        """
        # 第一个访问的URL
        self.visited_urls = [homepage]
        # 记录当前方法URL指针
        self.cur = 0
        # 记录当前数组的最后一个URL指针
        self.last = 0

    def visit(self, url: str) -> None:
        self.cur += 1
        # 当前节点小于数组的长度，说明我们需要更新访问数组的记录，当前index后的我们不再需要
        if len(self.visited_urls) > self.cur:
            self.visited_urls[self.cur] = url
        # 当前节点大于数组长度，及我们已经在当前访问记录的最后一个了，有新的URL加入，访问数组加入新的URL
        else:
            self.visited_urls.append(url)
        # 更新最后一个URL对应的的index
        self.last = self.cur

    def back(self, steps: int) -> str:
        # 更新当前index，最小为0
        self.cur = max(0, self.cur - steps)
        # 直接提取后退完成后当前index对应的URL
        return self.visited_urls[self.cur]

    def forward(self, steps: int) -> str:
        # 更新当前index，取最小值，最小为last指针index，因为last会记录访问记录中我们能走到的最远index
        self.cur = min(self.last, self.cur + steps)
        # 直接提取前进完成后当前index对应的URL
        return self.visited_urls[self.cur]


obj = BrowserHistory3("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
obj.visit("linkedin.com")
print(obj.forward(2))
print(obj.back(2))
print(obj.back(7))
