def is_safe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def solve(graph, path, pos):
    n = len(graph)
    if pos == n:
        return graph[path[-1]][path[0]] == 1
    for v in range(1, n):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if solve(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False

def hamiltonian_cycle(graph, names):
    n = len(graph)
    path = [-1] * n
    path[0] = 0
    if not solve(graph, path, 1):
        print("No Hamiltonian Cycle exists.")
        return
    path.append(path[0])
    print(" -> ".join(names[i] for i in path))

graph1 = [
    [0,1,1,0,1],
    [1,0,1,1,0],
    [1,1,0,1,0],
    [0,1,1,0,1],
    [1,0,0,1,0]
]
names1 = ["A","B","C","D","E"]
print("Graph 1:")
hamiltonian_cycle(graph1, names1)

graph2 = [
    [0,1,1,0,1],
    [1,0,1,1,0],
    [1,1,0,1,1],
    [0,1,1,0,1],
    [1,0,1,1,0]
]
names2 = ["T","M","S","H","C"]
print("\nGraph 2:")
hamiltonian_cycle(graph2, names2)
