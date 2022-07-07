#TODO: Description

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist                

graph = [
    [0,   5,  None, 10],
    [None,  0,  3,  None],
    [None, None, 0,   1],
    [None, None, None, 0]
]