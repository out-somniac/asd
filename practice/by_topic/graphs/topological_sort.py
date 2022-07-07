# Impementation of topological sorting a graph
# Definition: "Topological sort of a directed graph is a linear ordering of its vertices 
# such that for every directed edge (u, v) from vertex u to vertex v, u comes before v in the ordering."
# Useful for:
#   - Finding strongly connected components

def top_sort_visit(graph, visited, result, u):
    visited[u] = True

    for v in graph[u]:
        if not visited[v]:
            top_sort_visit(graph, visited, result, v)
    
    result.append(u)

def topological_sort(graph):
    visited = [False for _ in graph]
    result = []

    for u in range(len(graph)):
        if not visited[u]:
            top_sort_visit(graph, visited, result, u)

    return result[::-1]

graph = [
    [1, 2],
    [2, 5],
    [3],
    [],
    [],
    [3, 4],
    [1, 5]
]
print(topological_sort(graph))