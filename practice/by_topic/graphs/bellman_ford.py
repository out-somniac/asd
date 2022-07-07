#TODO: Description

def bellman_ford(graph, source):
    n = len(graph)
    dist = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]

    dist[source] = 0
    
    # Relaxation step
    for u in range(n):
        for v in range(n):
            if graph[u][v] != None and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                prev[v] = u
    
    # Verification
    for u in range(n):
        for v in range(n):
            if graph[u][v] != None and dist[v] > dist[u] + graph[u][v]:
                dist[v] = -float("inf")

    return dist, prev

def reconstruct(graph, dist, prev, target):
    path = []
    curr = target
    while curr != None:
        path.append(curr)
        curr = prev[curr]
    return path[::-1]

graph = [
    [None, 4, None, None, None, None, 7, None, None],
    [4, None, None, None, None, None, 11, 20, None],
    [None, 9, None, 6, 2, None, None, None, None],
    [None, None, 6, None, 10, 5, None, None, None],
    [None, None, 2, 10, None, 15, None, 1, 5],
    [None, None, None, 5, 15, None, None, None, 12],
    [7, 11, None, None, None, None, None, 1, None],
    [None, 20, None, None, 1, None, 1, None, 3],
    [None, None, None, None, 5, 12, None, 3, None],
]

source, target = 0, 4
dist, prev = bellman_ford(graph, source)
print(reconstruct(graph, dist, prev, target))
