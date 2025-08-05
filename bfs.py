from collections import deque


def bfs(graph,start_node):
    # Set to keep track of visited nodes
    visited=set()

    #Initialize queue with the start node
    queue=deque()
    queue.append(start_node)
    visited.add(start_node)

    print("BFS Traversal Order:")

    #Loop through the queue
    while queue :
        current_node=queue.popleft()
        print(current_node,end=' ') #Process current node

        #Visit all unvisited neighbors
        for neighbor in graph.get(current_node,[]):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

#Example usage : Define the graph as an adjacency list
graph_input={
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G']
}

bfs(graph_input,'A')