import heapq  # For priority queue

def ucs(graph, start_node, goal_node):
    # Priority queue: (cost, node)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))

    visited = set()

    print("UCS Traversal Order:")

    while priority_queue:
        cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        print(f"{current_node}(Cost: {cost})", end=' ')
        visited.add(current_node)

        # Goal check
        if current_node == goal_node:
            print(f"\nGoal '{goal_node}' found with cost {cost}")
            return

        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor))

    print(f"\nGoal '{goal_node}' not found")

# Graph format: node: list of (neighbor, cost)
graph_input = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1), ('G', 3)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

ucs(graph_input, 'A', 'G')