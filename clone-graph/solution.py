"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        root = Node(node.val)
        graph = {node.val : root}

        queue = [node]
        while(queue):
            curr = queue.pop(0)

            for node in curr.neighbors:

                if node.val not in graph:
                    graph[node.val] = Node(node.val)
                    queue.append(node)

                graph[curr.val].neighbors.append(graph[node.val])
        return root
        
