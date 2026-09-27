
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, node1, node2, cost):
        self.graph[node1].append((node2, cost))
        self.graph[node2].append((node1, cost))
    
    def shortestDist(self, p, q):
        root = p
        parent = dict()
        dist = [float('inf')] * (len(self.graph)+1)
        dist[p] = 0
        parent[p] = None
        queue = deque()
        queue.append(root)
        while queue:
            curr_node = queue.popleft()
            # explore its childrens
            for child_node, cost in self.graph[curr_node]:
                if dist[child_node] > dist[curr_node] + cost:
                    dist[child_node] = dist[curr_node] + cost
                    parent[child_node] = curr_node
                    queue.append(child_node)
                   
        # to get the path and dist
        path = [q]
        end = q
        while parent[end]:
            path.append(parent[end])
            end = parent[end]
        
        return '->'.join(map(str, path[::-1])), dist[q]
    

if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 3, 5)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 4, 1)
    g.add_edge(2, 5, 3)
    # g.add_edge(5, 6, 5)
    g.add_edge(3, 6, 2)
    g.add_edge(4, 6, 1)
    g.add_edge(5, 6, 0)
    # g.add_edge(4, 5, 1)
    
    print(g.shortestDist(3, 5))
    