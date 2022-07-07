from queue import Queue

# Algorithm that checks if a graph is bipartite using bfs and an adjacency list representation
# Time complexity is O(V + E) since the main algorithm used is BFS

def complementary(color):
    return 1 - color

def is_bipartite(graph, start = 0):
    colors = [None for _ in graph] # None - not visited yet / 0, 1 - colors
    visited = [False for _ in graph]
    queue = Queue()

    colors[start] = 0
    visited[start] = True
    queue.put(start)

    while not queue.empty():
        u = queue.get()
        
        for v in graph[u]:
            if colors[v] == colors[u] and visited[v]:
                return False
            
            if not visited[v]:
                visited[v] = True
                colors[v] = complementary(colors[u])
                queue.put(v)
    
    return True
    
bipartite = [
    [3, 4],
    [3, 4],
    [3, 4],
    [0, 1, 2],
    [0, 1, 2],
]

not_bipartite = [
    [1, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 1, 3, 4],
    [0, 1, 2, 4],
    [0, 1, 2, 3]
]

assert(is_bipartite(bipartite) == True)
assert(is_bipartite(not_bipartite) == False)