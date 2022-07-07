# The following algorithm solves the problem of ordering edges of an undirected graph 
# in such a way that if we remove these edges in that order the graph will remain "connected" during each step.
# Since it uses a modified DFS it's time complexity is O(V^2) for the matrix representation

#TODO: descriptions

def order_edges(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    path = []

    def dfs_visit(graph, visited, path, u):
        visited[u] = True

        for v in range(u, len(graph)):
            if graph[u][v]:
                if not visited[v]:
                    visited[v]= True
                    dfs_visit(graph, visited, path, v)
                path.append((u, v))

    for u in range(n):
        if not visited[u]:
            dfs_visit(graph, visited, path, u)
    
    return path

graph = [
    [False, True,  True,  False, False, False],
    [True,  False, True,  False, False, True],
    [True,  True,  False, True,  False, False],
    [False, False, True,  False, True,  True],
    [False, False, False, True,  False, True],
    [False, True,  False, True,  True,  False]
]

print(order_edges(graph))