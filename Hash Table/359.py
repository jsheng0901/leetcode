class Logger1:

    def __init__(self):
        self.message_to_time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Time O(n)
        Space O(n)  n -> number of unique message
        字典存储message到最新的timestamp的信息，每次来新的log的时候check一下是否存在，如果存在则check是否在10s之内，在则不能print，
        不在则可以print，同时更新最新对应时间。
        """
        res = False
        # 如果在则check
        if message in self.message_to_time:
            # 超过10s，可以返回
            if timestamp - self.message_to_time[message] >= 10:
                self.message_to_time[message] = timestamp
                res = True
        # 不在，说明是全新的message，直接返回
        else:
            self.message_to_time[message] = timestamp
            res = True

        # 其它情况都不能返回
        return res


class Logger2:

    def __init__(self):
        self.messages = set()
        self.queue = []

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Time O(n)
        Space O(n + m) n -> number of unique message, m -> number message in 10 timestamp
        用列队存储一个10s的滑动窗口，列队里面从头到底的时间都在10s内，如果来的新的log大于列队头的timestamp 10s，
        则说明之前的过期了，更新列队，同时更新记录unique message的集合。
        再check一遍新来的message是不是存在过，如果存在过说明一定是duplicate，直接返回false，
        如果不存在说明是全新的，返回true，同时更新集合和入列队。
        """
        # 检查列队头
        while self.queue:
            mes, ts = self.queue[0]
            # 如果列对头expire，弹出列队
            if timestamp - ts >= 10:
                self.queue.pop(0)
                self.messages.remove(mes)
            # 相反直接结束check
            else:
                break
        # 如果全新message，更新并返回true
        if message not in self.messages:
            self.queue.append((message, timestamp))
            self.messages.add(message)
            return True
        # 如果duplicate，返回false
        else:
            return False


# Your Logger object will be instantiated and called as such:
obj = Logger2()
logs = [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
for log in logs:
    print(obj.shouldPrintMessage(log[0], log[1]))
