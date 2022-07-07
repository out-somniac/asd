# Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
# Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
# na wyspę wynosi 8, koszt przeprawy promowej wynosi 5, za przejście mostem trzeba wnieść
# opłatę 1. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
# transportu na inny oraz minimalizuje koszt podróży.
# Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
# oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
# zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
# nie istnieje, funkcja powinna zwrócić wartość None.
# Przykład Dla tablicy
# G1 = [ 
#   [0,5,1,8,0,0,0 ],
#   [5,0,0,1,0,8,0 ],
#   [1,0,0,8,0,0,8 ],
#   [8,1,8,0,5,0,1 ],
#   [0,0,0,5,0,1,0 ],
#   [0,8,0,0,1,0,5 ],
#   [0,0,8,1,0,5,0 ] 
# ]
# funkcja islands(G1, 5, 2) powinna zwrócić wartość 13.

#TODO: Solution description

from os import truncate
from queue import PriorityQueue

def islands(graph, start, end):
    n = len(graph)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    queue = PriorityQueue()

    dist[start] = 0
    queue.put((dist[start], start))

    while not queue.empty():
        d, u = queue.get()
        visited[u] = True
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                new_dist = dist[u] + graph[u][v]
                old_dist = dist[v]
                # Here we modify the relaxation condition to only relaxe the edge
                # when the method of transportation of (u, v) is different than the method of (w, u)
                # where w is the parent of u
                if new_dist < old_dist and ( parent[u] == None or graph[parent[u]][u] != graph[u][v] ):
                    dist[v] = new_dist
                    parent[v] = u
                    queue.put((dist[v], v))

    sum = 0
    curr = end
    while curr != None:
        if parent[curr] != None:
            sum += graph[parent[curr]][curr]
        curr = parent[curr]
    return sum

graph = [
    [0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 0, 8],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0]
]
start = 5
end = 2
print( islands(graph, start, end) )