class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            # 双向链表的head是第一个元素
            # 双向链表的最后一个元素是tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1

    def delete(self, data):
        current = self.head
        # current先从head开始
        node_deleted = False
        if current is None:
            # 如果head是None
            node_deleted = False
        elif current.data == data:
            # 当前节点如果是要删除的节点,也就是head是要删除的节点
            # head移动指向到下一个节点
            # head的前一个节点是None
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            # 如果tail是要删除的节点
            # tail移动为他的前一个元素，他的后一个元素是None
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            # 非head 非tail
            while current:
                if current.data == data:
                    # 如果current是要删除的节点
                    # current的前一个元素的next是current的next
                    # current的后一个元素的prev是current的prev
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                # 如果当前不相等，则current移动
                current = current.next
        if node_deleted:
            self.count -= 1

    def iter(self):
        # 这是一个生成器，生成一个可迭代对象
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
        return False


dwords = DoublyLinkedList()
dwords.append('egg')
dwords.append('ham')

for i in dwords.iter():
    print(i)

print(dwords.contain('egg'))

