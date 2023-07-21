class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            # 非首节点
            self.head.next = node
            self.head = node
        else:
            # 首节点
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.size += 1

    # def delete(self, data):
    #     current = self.tail
    #     prev = self.tail
    #     while current:
    #         # 环形链表，current不会为None，可能会造成无限循环
    #         if current.data == data:
    #             # 当前节点找到了，且当前节点是tail, tail迁移，head指回tail
    #             if current == self.tail:
    #                 self.tail = current.next
    #                 self.head.next = self.tail
    #             else:
    #                 prev.next = current.next
    #             self.size -= 1
    #             return
    #         prev = current
    #         current = current.next
    def delete(self, data):
        current = self.tail
        prev = self.tail
        while prev == current or prev != self.head:
            # prev current都在第一个节点上
            # 或者prev没有移动回来（循环结束条件）
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next


words = Circur