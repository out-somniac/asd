#TODO: Descriptions

class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0

def find(node: Node):
    if not node.parent == node:
        node.parent = find(node.parent)
    return node.parent

def union(node_x: Node, node_y: Node):
    root_x = find(node_x)
    root_y = find(node_y)
    if root_x == root_y:
        return

    if root_x.rank > root_y.rank:
        root_y.parent = root_x
    else:
        root_x.parent = root_y
        if root_x.rank == root_y.rank:
            root_y.rank += 1