import heapq

def a_star_search(graph, start, goal, heuristic):
    """
    A* Tree Search
    f(n) = g(n) + h(n)
    """
    # Priority Queue: (f(n), g(n), node, path)
    frontier = [(heuristic[start], 0, start, [start])]
    explored = set()

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        # Goal test
        if current == goal:
            return path, g   # Return path and total cost

        if current in explored:
            continue
        explored.add(current)

        # Expand neighbors
        for neighbor, cost in graph[current]:
            if neighbor not in explored:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(frontier, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float("inf")  # No path found


# Example Graph (Adjacency List with costs)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 5)],
    'G': []
}

# Heuristic values (straight-line estimates to goal 'G')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'F': 3,
    'G': 0
}

# Run A* Search
path, cost = a_star_search(graph, 'A', 'G', heuristic)
print("Path found:", path)
print("Total cost:", cost)
