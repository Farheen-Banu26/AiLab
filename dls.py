def dls(graph, start_node, goal_node, limit):
    # Stack stores tuples of (node, current_depth)
    stack = [(start_node, 0)]
    visited = set()

    print("DLS Traversal Order:")

    while stack:
        current_node, depth = stack.pop()

        if current_node not in visited:
            print(current_node, end=' ')  # Process current node
            visited.add(current_node)

            # Goal check (optional)
            if current_node == goal_node:
                print(f"\nGoal '{goal_node}' found at depth {depth}")
                return True

            # If depth limit not reached, add neighbors
            if depth < limit:
                for neighbor in reversed(graph.get(current_node, [])):
                    stack.append((neighbor, depth + 1))

    print(f"\nGoal '{goal_node}' not found within depth limit {limit}")
    return False

# Define the graph
graph_input = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Call DLS with a depth limit of 2
dls(graph_input, 'A', 'G', 2)


