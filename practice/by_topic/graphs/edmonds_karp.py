from queue import Queue
# TODO: Descriptions
# The following is an implementation of the ford-fulkerson network flow algorithm.

def bfs(graph, parent, source, sink):
    visited = [False for _ in graph]
    queue = Queue()
    
    visited[source] = True
    queue.put(source)

    while not queue.empty():
        u = queue.get()
        for v in range(0, len(graph)):
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
                if v == sink:
                    return True
    
    return False

def FordFulkerson(graph, source, sink):
    parent = [None for _ in graph]
    max_flow = 0

    while bfs(graph, parent, source, sink):
        path_flow = float("inf")
        curr = sink
        while curr != source:
            path_flow = min(path_flow, graph[parent[curr]][curr])
            curr = parent[curr]
        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

    return max_flow

graph = [
    [0, 16, 13, 0,  0,  0],
    [0, 0,  10, 12, 0,  0],
    [0, 4,  0,  0,  14, 0],
    [0, 0,  9,  0,  0,  20],
    [0, 0,  0,  7,  0,  4],
    [0, 0,  0,  0,  0,  0]
]
source = 0
sink = 5
print(FordFulkerson(graph, source, sink))