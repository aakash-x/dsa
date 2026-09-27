
from collections import deque
from typing import Iterable

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)
    
    __repr__ = __str__
        
class Tree:
    def __init__(self, items: Iterable):
        self.root = None
        self.level = 0
        self.dq = deque()
        i = 0
        while i < len(items):
            node_count = pow(2, self.level)
            if not self.root:
                self.root = Node(items[i])
                self.dq.append(self.root)
                self.level += 1
                i += 1
                continue
            while node_count and i < len(items):
                top = self.dq.popleft()
                top.left = Node(items[i])
                self.dq.append(top.left)
                if i+1 < len(items):
                    top.right = Node(items[i+1])
                    self.dq.append(top.right)
                i += 2
                node_count -=2
            self.level += 1

def LevelOrderTraversal(root: Node):
    level = [-1] * len(tree)
    parent = [-1] * len(tree)
    queue = deque()
    lev = 0
    if root:
        queue.append(root)
        level[root.val] = lev
    while queue:
        count = pow(2, lev)
        for _ in range(count):
            if queue:
                top = queue.popleft()
                if top.val:
                    level[top.val] = lev
                    if top.left and top.left.val:
                        parent[top.left.val] = top.val
                        queue.append(top.left)
                    if top.right and top.right.val:
                        parent[top.right.val] = top.val
                        queue.append(top.right)
        lev += 1
    return level, parent

def shortestPath(root: Node, p, q):
    level, parent = LevelOrderTraversal(root)
    dist = 0
    while level[p] != level[q]:
        if level[p] < level[q]:
            q = parent[q]
        else:
            p = parent[p]
        dist += 1
    while p != q:
        dist += 2
        p = parent[p]
        q = parent[q]
    
    return dist
    
if __name__ == '__main__':
    tree = [3, 2, 8, 4, 5, 7, 6, None, None, 9]            
    t = Tree(tree)
    ans = shortestPath(t.root, 4, 7)
    print(ans)