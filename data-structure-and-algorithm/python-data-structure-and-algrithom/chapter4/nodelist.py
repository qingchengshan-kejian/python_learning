class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# 链表的链接是手动的
# 内部操作暴露在外
# n1 = Node('eggs')
# n2 = Node('ham')
# n3 = Node('spam')
# n1.next = n2
# n2.next = n3

# print(n1)
# print(n2)
# print(n3)

# # 遍历一个链表，从第一个节点开始
# current = n1
# while current:
#     print(current)
#     current = current.next

# 单向链表
class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    # 添加节点的方法函数
    def append(self, data):
        # 在Node里封装data
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail # 这个tail其实是第一个放进去的node节点
            # 每次插入都要从第一个开始，一直移动current到最后一个，next为None然后给这个节点的next属性赋值。
            while current.next:
                current = current.next
            current.next = node

    def fastappend(self, data):
        # 在Node里封装data
        node = Node(data)
        if self.head:
            # head指向的其实是最后一个插入的节点，如果head指向的节点不是None，head后插入节点
            # head 移动指向到新节点
            self.head.next = node
            self.head = node
        else:
            # 如果head指向None，也就是说插入的是第一个节点
            # tail head 都指向这个节点
            self.tail = node
            self.head = node
        self.size += 1

    def size(self):
        # 这个size的求解方法，是遍历链表。
        # 开销有点大，可以在操作增加节点的时候，对节点数计数
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count

    def iter(self):
        # 这是一个生成器，生成一个可迭代对象
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                # 找到了，且是首个节点，tail移动到后面一个节点
                if current == self.tail:
                    self.tail = current.next
                # 找到了，不是首个节点
                else:
                    # prev 直接指向 current的下一个节点
                    prev.next = current.next
                self.size -= 1
                return
            # 如果data没找到，prev 移到current，current移动到下一个
            prev = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        '''清除掉整个链表'''
        self.tail = None
        self.head = None





# words = SinglyLinkedList()
# words.append('egg')
# words.append('ham')
# words.append('spam')
# current = words.tail
# while current:
#     print(current)
#     current = current.next

words = SinglyLinkedList()
words.fastappend('egg')
words.fastappend('ham')
words.fastappend('spam')
# 遍历数组还是暴露在外的，可以把遍历操作封装在类里面
# current = words.tail
# while current:
#     print(current)
#     current = current.next

words.delete('egg')
for word in words.iter():
    print(word)

# print(words.size())

print(words.size)
print(words.search("egg"))
print(words.search("ham"))




