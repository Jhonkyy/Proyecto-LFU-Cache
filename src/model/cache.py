from src.model.listas_ligadas import DoublyLinkedList, Node
from collections import defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.freq_map = defaultdict(DoublyLinkedList)
        self.min_freq = 0

    def _update_freq(self, node):
        freq = node.freq
        self.freq_map[freq].pop(node)
        if self.min_freq == freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int):
        if self.capacity == 0:
            return
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update_freq(node)
        else:
            if len(self.node_map) >= self.capacity:
                removed_node = self.freq_map[self.min_freq].pop()
                del self.node_map[removed_node.key]
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.freq_map[1].append(new_node)
            self.min_freq = 1
