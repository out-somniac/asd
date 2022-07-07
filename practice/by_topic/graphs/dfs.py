# Depth first search
# Useful for:
#   - Check if a graph is connected
#   - Check if a graph is bipartite
#   - Detecting cycles
#   - Topological sorting
#   - Finding the euler cycle in a graph
#   - Finding strongly connected components
#   - Finding bridges
#   - Finding points of articulation

def dfs_adj(graph):
    """
    Depth-first search implementation on a graph with adjacency list representation.
    The time complexity of this algorithm is O(V + E)
    """
    visited = [False for _ in graph]
    parent = [None for _ in graph]
    time = 0

    def dfs_adj_visit(graph, visited, parent, u):
        nonlocal time
        time += 1
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs_adj_visit(graph, visited, parent, v)
        time += 1

    for u in range(len(graph)):
        if not visited[u]:
            dfs_adj_visit(graph, visited, parent, u)


def dfs_mat(graph):
    """
    Depth-first search algorithm implemented using the adjacency matrix representationn
    The time complexity of this algorithm is O(V^2)
    """
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0

    def dfs_mat_visit(graph, visited, parent, u):
        nonlocal time
        time += 1
        visited[u] = True

        for v in range(0, len(graph)):
            if graph[u][v] > 0 and not visited[v]:
                print(u, v)
                parent[v] = u
                dfs_mat_visit(graph, visited, parent, v)
        time += 1

    for u in range(n):
        if not visited[u]:
            dfs_mat_visit(graph, visited, parent, u)

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

dfs_adj(graph_adj)
dfs_mat(graph_mat)