class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return None
        if not node:
            node = self.head.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
