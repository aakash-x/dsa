# design the class in the most optimal way

class Node:
    def __init__(self, key, val):
        self.key = key        
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
      
    def __init__(self, cap):
        #code here
        self.cap = cap
        self.map = dict()
        self.head = Node(-1, -1);
        self.tail = Node(-1, -1);
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def deleteNode(self, node):
        if not self.head.next:
            return 
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
    def insertAtHead(self, node):
        # delink current head, and add new first node
        self.head.next.prev = node
        node.next = self.head.next
        
        # new head operations
        node.prev = self.head
        self.head.next = node
        
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            # de link node from its current position
            self.deleteNode(node)
            # re insert same node at head
            self.insertAtHead(node)
            return node.val
        return -1
        

    def put(self, key, value):            
        if key in self.map:
            # if key already in map, then update its value
            node = self.map[key]
            node.val = value
            self.deleteNode(node)
            self.insertAtHead(node)
            return
                # if LRU capacity is full, remove last node
        if len(self.map) == self.cap:
            # delete a node from last
            node = self.deleteNode(self.tail.prev)
            del self.map[node.key]
        node = Node(key, value)
        self.insertAtHead(node)
        self.map[key] = node
            
            


if __name__ == "__main__":            
    with open("fileinput.txt", "r") as f:
        size = int(f.readline().strip())
        LRUCache = LRUCache(size)
        query = int(f.readline().strip())
        for line in f:
            line = line.strip()

            if line.startswith("PUT"):
                key, value = map(int, line.split()[1:])
                    LRUCache.put(int(key), int(value))
            elif line.startswith("GET"):
                key = int(line.split()[1:][0])
                print(LRUCache.get(int(key)))