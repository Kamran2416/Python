def astar(graph, start, goal, h):
    open_set = {start}
    came_from = {}
    g = {start: 0}
    f = {start: h[start]}

    while open_set:
        current = min(open_set, key=lambda x: f.get(x, float('inf')))

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_set.remove(current)

        for neighbor, cost in graph[current]:
            temp_g = g[current] + cost
            if neighbor not in g or temp_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = temp_g
                f[neighbor] = temp_g + h[neighbor]
                open_set.add(neighbor)

    return None
# Graph in form: node: [(neighbor, cost), ...]
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': [('E', 2)],
    'E': []
}

# Heuristic values (estimated cost to goal)
h = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 0
}

path = astar(graph, 'A', 'E', h)
print("Path:", path)
