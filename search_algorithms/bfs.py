"""
Traverse a graph using Breadth First Search (BFS).
"""

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

def bfs(graph, start):

    visited = []
    queue = [start]

    while queue:

        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                queue.append(neighbor)

    return visited

print(bfs(graph, "A"))