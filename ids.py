def dls(graph, current_node, goal_node, limit, visited):
    if current_node not in visited:
        print(current_node, end=' ')
        visited.add(current_node)

        if current_node == goal_node:
            return True

        if limit <= 0:
            return False

        for neighbor in graph.get(current_node, []):
            if dls(graph, neighbor, goal_node, limit - 1, visited):
                return True
    return False

def ids(graph, start_node, goal_node, max_depth):
    print("IDS Traversal Order:")

    for depth in range(max_depth + 1):
        visited = set()
        print(f"\nDepth Level {depth}: ", end='')
        if dls(graph, start_node, goal_node, depth, visited):
            print(f"\nGoal '{goal_node}' found at depth {depth}")
            return
    print(f"\nGoal '{goal_node}' not found within depth {max_depth}")


# Define the graph
graph_input = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Perform IDS with max depth 3
ids(graph_input, 'A', 'G', 3)