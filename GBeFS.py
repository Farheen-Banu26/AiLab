import heapq  # for priority queue

def greedy_best_first_search(graph, start, goal, heuristic):
    """
    graph: dictionary with adjacency list, e.g. {'A': [('B', cost), ('C', cost)], ...}
    start: starting node
    goal: goal node
    heuristic: dictionary with heuristic values for each node
    """
    # Priority queue stores (heuristic, node, path)
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start, [start]))
    
    visited = set()

    print("Greedy Best-First Search Traversal Order:")

    while priority_queue:
        h, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)

        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            return path

        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    print("\nGoal not reachable.")
    return None


# Example usage
graph = {
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}

# Example heuristic values (straight-line distance estimates to goal 'G')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

path = greedy_best_first_search(graph, 'A', 'G', heuristic)
print("Final Path:", path)
