def is_safe(node, graph, colors, c):
    for i in range(len(graph)):
        if graph[node][i] == 1 and colors[i] == c:
            return False
    return True

def solve(node, graph, m, colors):
    if node == len(graph):
        return True
    for c in range(1, m + 1):
        if is_safe(node, graph, colors, c):
            colors[node] = c
            if solve(node + 1, graph, m, colors):
                return True
            colors[node] = 0
    return False

def graph_coloring(graph, m, names):
    colors = [0] * len(graph)
    if not solve(0, graph, m, colors):
        print("No valid coloring possible.")
        return
    for i in range(len(graph)):
        print(f"{names[i]} -> Color {colors[i]}")

graph1 = [
    [0,1,1,0,1],
    [1,0,1,1,0],
    [1,1,0,1,0],
    [0,1,1,0,1],
    [1,0,0,1,0]
]
names1 = ["A","B","C","D","E"]
print("Graph 1 coloring:")
graph_coloring(graph1, 3, names1)

print()

graph2 = [
    [0,1,1,1,1],
    [1,0,1,1,1],
    [1,1,0,1,1],
    [1,1,1,0,1],
    [1,1,1,1,0]
]
names2 = ["T","M","S","H","C"]
print("Graph 2 coloring:")
graph_coloring(graph2, 5, names2)
