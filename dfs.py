from collections import deque

def dfs(graph, start_node):
    # Set to keep track of visited nodes
    visited = set()

    # Initialize stack with the start node
    stack = [start_node]

    print("DFS Traversal Order:")

    # Loop through the stack
    while stack:
        current_node = stack.pop()
        
        if current_node not in visited:
            print(current_node, end=' ')  # Process current node
            visited.add(current_node)

            # Push unvisited neighbors onto the stack (reversed for correct order)
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage: Define the graph as an adjacency list
graph_input = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

dfs(graph_input, 'A')