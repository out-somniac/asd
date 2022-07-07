from queue import Queue

# Breadth-first search
# Useful for : 
#   - Finding shortest paths in a graph without weights
#   - Checking if a graph is connected
#   - Detecting cycles
#   - Check a graph is bipartite

def bfs_adj(graph, start = 0):
    """
    Breadth-first search algorithm implemented using the adjacency list representationn
    The time complexity of this algorithm is O(V + E)
    Note: This function will only go throught one connected component of the graph.
        To execute bfs for all conected a loop going through all unvisited vertices must be added externally.
    """
    visited = [False for _ in graph]
    parent = [None for _ in graph]
    depth = [None for _ in graph]
    exec_queue = Queue()

    visited[start] = True
    depth[start] = 0
    exec_queue.put(start)

    while not exec_queue.empty():
        u = exec_queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                parent[v] = u
                exec_queue.put(v)
    
def bfs_mat(graph, start = 0):
    """
    Breadth-first search algorithm implemented using the adjacency matrix representationn
    The time complexity of this algorithm is O(V^2)
    Note: This function will only go throught one connected component of the graph.
        To execute bfs for all conected a loop going through all unvisited vertices must be added externally.
    """
    visited = [False for _ in graph]
    depth = [None for _ in graph]
    parent = [None for _ in graph]
    exec_queue = Queue()

    visited[start] = True
    depth[start] = 0
    exec_queue.put(start)

    while not exec_queue.empty():
        u = exec_queue.get()
        for v in range(0, len(graph)):
            if graph[u][v] > 0 and not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                parent[v] = u
                exec_queue.put(v)
    
graph_adj = [ 
    [2, 3, 5], 
    [3, 4, 6], 
    [0, 4, 7], 
    [0, 1, 8],
    [1, 2, 9], 
    [0, 6, 9], 
    [1, 5, 7], 
    [2, 6, 8], 
    [3, 7, 9], 
    [4, 5, 8] 
]

graph_mat = [
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
]

bfs_adj(graph_adj)
bfs_mat(graph_mat)