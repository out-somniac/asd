from queue import Queue

# Algorithm that finds the shortest path from vertices s to t in an unweighted graph
# Since the main backbone of this algorithm is BFS the time complexity is O(V + E)

def reconstruct(parent, t):
    """ This function reconstructs the solution from a previously created parent array. The time complexity of this step is O(V) """
    curr = t
    path = []

    while curr != None:
        path.append(curr)
        curr = parent[curr]
    
    return path[::-1]

def shortes_path(graph, s, t):
    """ Modified BFS that exits if it discovers the node t, since hitting node t means that we've build the parrent array from s to t. """
    visited = [False for _ in graph]
    parent = [None for _ in graph]
    queue = Queue()

    visited[s] = True
    parent[s] = None
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        
        if u == t:
            return reconstruct(parent, t)

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.put(v)

graph = [
    [1, 3],
    [0, 2],
    [1],
    [0, 4, 7],
    [3, 5, 6 ,7],
    [4, 6],
    [4, 5, 7],
    [3, 4, 6]
]

print(shortes_path(graph, 0, 7))