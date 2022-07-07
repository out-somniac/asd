#TODO: Descriptions

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x == root_y:
        return

    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

def kruskal(edges, n):
    result = []
    edges.sort(key=lambda e: e[0])

    # Usef for the union-find structure
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    for cost, u, v in edges:
        if find(u, parent) != find(v, parent):
            result.append((cost, u, v))
            union(u, v, parent, rank)
    return result


edges = [
    (1,7,6), (2,8,2), (2,6,5),
    (4,0,1), (4,2,5), (6,8,6),
    (7,2,3), (7,7,8), (8,0,7),
    (8,1,2), (9,3,4), (10,5,4),
    (11,1,7), (14,3,5)
]
edges = kruskal(edges, 9)
sum = 0
for e in edges:
    sum += e[0]
print(edges)
print(sum)