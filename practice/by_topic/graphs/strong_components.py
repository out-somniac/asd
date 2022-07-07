# An algorithm that finds strongly connected components in a graph
# TODO: Build algorithm
def transpose_adj(graph):
    transpose = [[] for _ in graph]
    for u, adj in enumerate(graph):
        for v in adj:
            transpose[v].append(u)
    return transpose

def transpose_mat(graph):
    transpose = [[False for _ in graph] for _ in graph]
    n = len(graph)
    for u in range(n):
        for v in range(n):
            transpose[v][u] = graph[u][v]
    return transpose

graph_adj = [[1, 2], [0, 3], [0, 3], [5], [2, 5], [3], [4], [5, 6], [6, 7, 8]]
graph_mat = [[False for _ in graph_adj] for _ in graph_adj]
for u, adj in enumerate(graph_adj):
    for v in adj:
        graph_mat[u][v] = True
