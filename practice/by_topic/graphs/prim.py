from queue import PriorityQueue

#TODO: Descriptions
#TODO: U Sure?

def matrix_prim(graph):
    queue = PriorityQueue()
    visited = [False for _ in graph]
    edges = []

    visited[0] = True
    for v in range(len(graph)):
        if not graph[0][v] < 0:
            queue.put((graph[0][v], 0, v))
    count = 1

    while not queue.empty() and count <= len(graph):
        cost, u, v = queue.get()
        if not visited[v]:
            visited[v] = True
            count += 1
            edges.append((cost, u, v))
            for w in range(len(graph)):
                if not graph[v][w] < 0:
                    queue.put((graph[v][w], v, w))
    return edges

def adj_prim(graph):
    queue = PriorityQueue()
    visited = [False for _ in graph]
    edges = []
    
    visited[0] = True
    for v, cost in graph[0]:
        queue.put((cost, 0, v))
    vert_count = 1

    while not queue.empty() and vert_count <= len(graph):
        cost, u, v = queue.get()
        if not visited[v]:
            visited[v] = True
            edges.append((cost, u, v))
            vert_count += 1
            for w, new_cost in graph[v]:
                queue.put((new_cost, v, w))
    return edges

adjacency = [
    [(1, 2), (2, 5), (3, 2), (4, 3)],
    [(0, 2), (3, 0)],
    [(0, 5), (4, 6), (3, 1)],
    [(0, 2), (1, 0), (2, 1), (3, 4), (5, 8)],
    [(0, 3), (2, 6), (3, 4)],
    [(3, 8)]
]

matrix = [[-1 for _ in adjacency] for _ in adjacency]
for u, adjacent in enumerate(adjacency):
    for v, cost in adjacent:
        matrix[u][v] = cost

#edges = matrix_prim(matrix)
edges = adj_prim(adjacency)
print(edges)