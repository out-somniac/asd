from queue import PriorityQueue

#TODO: descriptions

# Dijkstra's Single Source Shortest Path algorithm
# It's time complexity is O(Elog(V))

def dijkstra_adj(graph, source):
    dist = [float("inf") for _ in graph]
    prev = [None for _ in graph]
    visited = [False for _ in graph]
    queue = PriorityQueue()

    dist[source] = 0
    queue.put((dist[source], source))

    while not queue.empty():
        d, u = queue.get()
        visited[u] = True
        for v, weight in graph[u]:
            if not visited[v]:
                old_cost = dist[v]
                new_cost = dist[u] + weight
                if new_cost < old_cost:
                    dist[v] = new_cost
                    prev[v] = u
                    queue.put((dist[v], v))
    return dist, prev

def dijkstra_mat(graph, source):
    dist = [float("inf") for _ in graph]
    prev = [None for _ in graph]
    visited = [False for _ in graph]
    queue = PriorityQueue()

    dist[source] = 0
    queue.put((dist[source], source))
    
    while not queue.empty():
        d, u = queue.get()
        visited[u] = True

        for v in range(0, len(graph)):
            if graph[u][v] != None and not visited[v]:
                old_cost = dist[v]
                new_cost = dist[u] + graph[u][v]
                if new_cost < old_cost:
                    dist[v] = new_cost
                    prev[v] = u
                    queue.put((dist[v], v))
    return dist, prev

def reconstruct(graph, dist, prev, target):
    path = []
    curr = target
    while curr != None:
        path.append(curr)
        curr = prev[curr]
    return path[::-1]

# (destination, weight)
graph_adj = [
    [(1, 4), (6, 7)],
    [(0, 4), (6, 11), (7, 20)],
    [(1, 9), (3, 6), (4, 2)],
    [(2, 6), (4, 10), (5, 5)],
    [(2, 2), (3, 10), (5, 15), (7, 1), (8, 5)],
    [(3, 5), (4, 15), (8, 12)],
    [(0, 7), (1, 11), (7, 1)],
    [(6, 1), (1, 20), (4, 1), (8, 3)],
    [(4, 5), (7, 3), (5, 12)]
]

graph_mat = [[None for _ in graph_adj] for _ in graph_adj]
for u, adj in enumerate(graph_adj):
    for v, weight in adj:
        graph_mat[u][v] = weight

source, target = 0, 4
dist, prev = dijkstra_mat(graph_mat, source)
# dist, prev = dijkstra_adj(graph_mat, source)
print(reconstruct(graph_adj, dist, prev, target))
