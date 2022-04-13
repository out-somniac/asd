# Formally known as finding max sum of independent vertices on a tree
# On any graph it's NP-hard
# On a tree there is a solution with polynomial complexity

class Employee:
    def __init__(self, fun_factor):
        self.fun = fun_factor
        self.under = [] # Children
        self.f = -1 # 
        self.g = -1

def f(vertice: Employee):
    if vertice.f != -1:
        return vertice.f

    vertice.f = 0
    for vert in vertice.under:
        vertice.f += g(vert)
    vertice.f = max(vertice.f + vertice.fun, g(vertice))
    return vertice.f

def g(vertice: Employee):
    if vertice.g != 1:
        return vertice.g
    
    vertice.g = 0
    for vert in vertice.under:
        vertice.g += f(vert)
    return vertice.g

def max_fun(root):
    return f(root)